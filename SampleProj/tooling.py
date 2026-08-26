import json
import os
import sqlite3

_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")
_COLLEGE_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "college.db")

# Known college tables for schema inspection
_COLLEGE_TABLES = ["students", "fees_status", "marks"]


def _load_db():
    with open(_DB_PATH, encoding="utf-8") as f:
        return json.load(f)["items"]


def get_all_items():
    """Return every item in the database with name, type, and price."""
    return _load_db()


def get_item_by_name(name):
    """Look up a single item by name (case-insensitive). Returns dict or None."""
    name_lower = name.strip().lower()
    for item in _load_db():
        if item["name"].lower() == name_lower:
            return item
    return None


def get_items_by_type(item_type):
    """Return all items matching a given type: fruit or vegetable."""
    type_lower = item_type.strip().lower()
    return [item for item in _load_db() if item["type"].lower() == type_lower]


# ── College DB tools ────────────────────────────────────────────────────────

def get_schema(table_name=None):
    """Return column metadata for one or all college tables.

    Args:
        table_name: Optional table name (students | fees_status | marks).
                    If omitted, returns schema for all three tables.

    Returns:
        JSON string: {"schema": {<table>: [<col_info>, ...]}} or
                     {"warning": "...", "schema": {}} on error.
    """
    tables = (
        [table_name.strip().lower()]
        if table_name
        else _COLLEGE_TABLES
    )

    schema = {}
    try:
        conn = sqlite3.connect(_COLLEGE_DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        for tbl in tables:
            if tbl not in _COLLEGE_TABLES:
                schema[tbl] = {"warning": f"Unknown table '{tbl}'. Valid tables: {_COLLEGE_TABLES}"}
                continue
            cur.execute(f"PRAGMA table_info({tbl})")
            rows = cur.fetchall()
            schema[tbl] = [
                {"cid": r["cid"], "name": r["name"], "type": r["type"],
                 "notnull": bool(r["notnull"]), "pk": bool(r["pk"])}
                for r in rows
            ]
        conn.close()
    except Exception as exc:
        return json.dumps({"warning": str(exc), "schema": {}})

    return json.dumps({"schema": schema})


def query_college_db(sql, limit=100):
    """Execute a read-only SQL SELECT against the college SQLite database.

    The LLM must supply valid SQLite SELECT syntax. INSERT / UPDATE / DELETE /
    DROP and other write statements are rejected for safety.

    Args:
        sql   : A SQLite SELECT statement to run against college.db.
        limit : Maximum number of rows to return (default 100, max 500).

    Returns:
        JSON string: {"columns": [...], "rows": [...], "row_count": N} on
                     success, or {"warning": "...", "rows": [], "row_count": 0}
                     on error or disallowed statement.
    """
    _ALLOWED_PREFIX = ("select", "with", "explain", "pragma")
    sql_stripped = sql.strip()
    if not sql_stripped.lower().split()[0] in _ALLOWED_PREFIX:
        return json.dumps({
            "warning": "Only SELECT (and WITH/EXPLAIN/PRAGMA) statements are allowed.",
            "rows": [],
            "row_count": 0,
        })

    # Clamp limit
    try:
        limit = max(1, min(int(limit), 500))
    except (TypeError, ValueError):
        limit = 100

    # Inject LIMIT if not already present
    sql_lower = sql_stripped.lower()
    if "limit" not in sql_lower:
        sql_stripped = f"{sql_stripped} LIMIT {limit}"

    try:
        conn = sqlite3.connect(_COLLEGE_DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql_stripped)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description] if cur.description else []
        conn.close()
        result = [dict(row) for row in rows]
        return json.dumps({"columns": columns, "rows": result, "row_count": len(result)})
    except Exception as exc:
        return json.dumps({"warning": str(exc), "rows": [], "row_count": 0})


# ── Gemini function declarations ────────────────────────────────────────────

GET_ALL_ITEMS_DECL = {
    "name": "get_all_items",
    "description": (
        "Retrieve the complete list of all fruits and vegetables "
        "available in the store, including their type and price per kg in INR."
    ),
    "parameters": {"type": "object", "properties": {}, "required": []},
}

GET_ITEM_BY_NAME_DECL = {
    "name": "get_item_by_name",
    "description": (
        "Look up a specific fruit or vegetable by its exact name "
        "and return its type and price per kg in INR."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Name of the item to look up, e.g. Tomato or Apple.",
            }
        },
        "required": ["name"],
    },
}

GET_ITEMS_BY_TYPE_DECL = {
    "name": "get_items_by_type",
    "description": (
        "Retrieve all items belonging to a specific category. "
        "Use item_type=fruit for fruits or item_type=vegetable for vegetables."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "item_type": {
                "type": "string",
                "description": "Category to filter by: fruit or vegetable.",
            }
        },
        "required": ["item_type"],
    },
}

GET_SCHEMA_DECL = {
    "name": "get_schema",
    "description": (
        "Return the column names and data types for one or all tables in the college "
        "SQLite database (students, fees_status, marks). "
        "Call this before writing SQL so you know the exact column names. "
        "Omit table_name to get the full schema for all three tables at once."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "table_name": {
                "type": "string",
                "description": (
                    "Optional. One of: students, fees_status, marks. "
                    "Omit to retrieve the schema for all tables."
                ),
            }
        },
        "required": [],
    },
}

QUERY_COLLEGE_DB_DECL = {
    "name": "query_college_db",
    "description": (
        "Execute a read-only SQL SELECT statement against the college SQLite database "
        "(college.db) which contains three tables: students (personal info), "
        "fees_status (semester fee payments), and marks (6-subject marks per semester). "
        "You must write valid SQLite SELECT syntax. Write operations (INSERT, UPDATE, "
        "DELETE, DROP) are blocked. Use get_schema first to confirm column names."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "sql": {
                "type": "string",
                "description": (
                    "A valid SQLite SELECT statement to run against college.db. "
                    "Example: SELECT first_name, last_name, cgpa FROM students ORDER BY cgpa DESC"
                ),
            },
            "limit": {
                "type": "integer",
                "description": (
                    "Maximum number of rows to return. Defaults to 100. Maximum allowed is 500."
                ),
            },
        },
        "required": ["sql"],
    },
}

ALL_TOOL_DECLARATIONS = [
    GET_ALL_ITEMS_DECL,
    GET_ITEM_BY_NAME_DECL,
    GET_ITEMS_BY_TYPE_DECL,
    GET_SCHEMA_DECL,
    QUERY_COLLEGE_DB_DECL,
]

TOOL_DISPATCH = {
    "get_all_items": get_all_items,
    "get_item_by_name": get_item_by_name,
    "get_items_by_type": get_items_by_type,
    "get_schema": get_schema,
    "query_college_db": query_college_db,
}


# ── MCP Server (FastMCP) ─────────────────────────────────────────────────────

import warnings
warnings.filterwarnings("ignore")          # suppress pydantic / deprecation noise

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ItemDatabase")


@mcp.tool()
def mcp_get_all_items() -> str:
    """Retrieve the complete list of all fruits and vegetables available in the
    store, including their type and price per kg in INR."""
    return json.dumps(get_all_items(), ensure_ascii=False)


@mcp.tool()
def mcp_get_item_by_name(name: str) -> str:
    """Look up a specific fruit or vegetable by its exact name and return its
    type and price per kg in INR.

    Args:
        name: Name of the item to look up, e.g. Tomato or Apple.
    """
    result = get_item_by_name(name)
    return json.dumps(result, ensure_ascii=False) if result else json.dumps({"result": "Not found."})


@mcp.tool()
def mcp_get_items_by_type(item_type: str) -> str:
    """Retrieve all items belonging to a specific category (fruit or vegetable).

    Args:
        item_type: Category to filter by — use 'fruit' or 'vegetable'.
    """
    return json.dumps(get_items_by_type(item_type), ensure_ascii=False)


@mcp.tool()
def mcp_get_schema(table_name: str = "") -> str:
    """Return column names and data types for one or all college DB tables.
    Tables available: students, fees_status, marks.
    Leave table_name empty to get the schema for all three tables.

    Args:
        table_name: Optional. One of: students, fees_status, marks. Leave blank for all.
    """
    return get_schema(table_name if table_name else None)


@mcp.tool()
def mcp_query_college_db(sql: str, limit: int = 100) -> str:
    """Execute a read-only SELECT statement against the college SQLite database
    (college.db). Write operations (INSERT, UPDATE, DELETE, DROP) are blocked.
    Call mcp_get_schema first to confirm exact column names.

    Args:
        sql:   A valid SQLite SELECT statement.
        limit: Max rows to return (default 100, max 500).
    """
    return query_college_db(sql, limit)


if __name__ == "__main__":
    mcp.run()
