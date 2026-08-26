"""
synth_data.py
-------------
Generates synthetic college student data for a South Indian college and stores
it in a local SQLite database (college.db).

Tables created:
  1. students          - personal information
  2. fees_status       - fee payment records per semester
  3. marks             - marks for 6 subjects per semester

Usage:
    python synth_data.py
"""

import sqlite3
import random
from faker import Faker

# South-Indian name pools

SOUTH_INDIAN_FIRST_NAMES = [
    # Tamil
    "Aravind", "Balaji", "Chandra", "Deepak", "Ezhil", "Gowtham", "Harish",
    "Ilavarasan", "Jeyakumar", "Karthik", "Logesh", "Murugan", "Naveen",
    "Oviya", "Priya", "Rajesh", "Senthil", "Tamilselvan", "Udhaya", "Vetri",
    "Anand", "Bharath", "Dinesh", "Gokul", "Jeeva", "Kiruthika", "Lavanya",
    "Meenakshi", "Nithya", "Pavithra", "Ramya", "Saranya", "Thilaga",
    "Vijaya", "Yamini", "Abinaya", "Banupriya", "Chandrika", "Devi",
    # Telugu
    "Aditya", "Bhavani", "Chaitanya", "Deepthi", "Eswar", "Geetha",
    "Hemanth", "Isha", "Jyothi", "Kavya", "Lakshmi", "Mahesh", "Naga",
    "Padmavathi", "Raghavendra", "Sravya", "Tejaswi", "Usha", "Vamsi",
    "Yamuna", "Arjun", "Bhargav", "Charan", "Divya", "Goutham",
    # Kannada
    "Akash", "Bharatesh", "Chethan", "Darshan", "Ganesh", "Harsha",
    "Indira", "Jagadish", "Kaveri", "Lokesh", "Manjunath", "Nandini",
    "Pooja", "Rakesh", "Shanthi", "Tejas", "Umesh", "Varsha", "Yashwanth",
    # Malayalam
    "Abhijith", "Bindu", "Chithra", "Deepa", "Greeshma", "Harikrishnan",
    "Indulekha", "Jithesh", "Keerthi", "Lekha", "Madhavan", "Neetha",
    "Parvathy", "Rahul", "Soumya", "Theertha", "Vishnu",
]

SOUTH_INDIAN_LAST_NAMES = [
    # Tamil-style
    "Murugan", "Rajan", "Krishnan", "Pillai", "Nair", "Iyer", "Iyengar",
    "Gounder", "Nadar", "Chettiar", "Thevar", "Pandian", "Selvam",
    # Telugu-style
    "Reddy", "Naidu", "Rao", "Sharma", "Varma", "Prasad", "Babu",
    "Raju", "Goud", "Chowdary", "Yadav", "Murthy",
    # Kannada-style
    "Gowda", "Shetty", "Hegde", "Naik", "Devegowda", "Patil",
    "Swamy", "Achar", "Bhat",
    # Malayalam-style
    "Menon", "Nambiar", "Kurup", "Namboothiri", "Thampi",
    "Varghese", "Thomas", "Mathew",
]

DEPARTMENTS = [
    "Computer Science", "Information Technology", "Electronics & Communication",
    "Mechanical Engineering", "Civil Engineering", "Electrical Engineering",
    "Biotechnology", "Chemical Engineering", "Mathematics", "Physics",
]

GRADUATION_YEARS = [2024, 2025, 2026, 2027]

fake = Faker("en_IN")


def south_indian_name():
    first = random.choice(SOUTH_INDIAN_FIRST_NAMES)
    last = random.choice(SOUTH_INDIAN_LAST_NAMES)
    return first, last


def random_phone():
    prefix = random.choice(["9", "8", "7", "6"])
    rest = "".join([str(random.randint(0, 9)) for _ in range(9)])
    return f"+91 {prefix}{rest}"


def random_email(first, last):
    first_clean = first.lower().replace(" ", "")
    last_clean = last.lower().replace(" ", "")
    domains = ["gmail.com", "yahoo.co.in", "outlook.com", "college.edu.in"]
    return f"{first_clean}.{last_clean}{random.randint(1, 99)}@{random.choice(domains)}"


def random_marks():
    marks = []
    for _ in range(6):
        if random.random() < 0.05:
            marks.append(random.randint(10, 34))
        else:
            marks.append(random.randint(35, 100))
    return marks


def fee_amount_for_dept(dept):
    base = {
        "Computer Science": 90000, "Information Technology": 85000,
        "Electronics & Communication": 88000, "Mechanical Engineering": 82000,
        "Civil Engineering": 78000, "Electrical Engineering": 80000,
        "Biotechnology": 95000, "Chemical Engineering": 83000,
        "Mathematics": 55000, "Physics": 52000,
    }
    return float(base.get(dept, 75000))


def create_tables(conn):
    cur = conn.cursor()
    cur.executescript("""
        PRAGMA journal_mode=WAL;

        CREATE TABLE IF NOT EXISTS students (
            student_id      TEXT PRIMARY KEY,
            roll_number     TEXT UNIQUE NOT NULL,
            first_name      TEXT NOT NULL,
            last_name       TEXT NOT NULL,
            gender          TEXT NOT NULL,
            date_of_birth   TEXT NOT NULL,
            email           TEXT UNIQUE NOT NULL,
            phone           TEXT NOT NULL,
            address         TEXT,
            city            TEXT,
            state           TEXT,
            department      TEXT NOT NULL,
            year_of_joining INTEGER NOT NULL,
            graduation_year INTEGER NOT NULL,
            cgpa            REAL
        );

        CREATE TABLE IF NOT EXISTS fees_status (
            fee_id          INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id      TEXT NOT NULL REFERENCES students(student_id),
            semester        INTEGER NOT NULL,
            total_fee       REAL NOT NULL,
            amount_paid     REAL NOT NULL,
            balance         REAL NOT NULL,
            payment_status  TEXT NOT NULL,
            payment_date    TEXT,
            payment_mode    TEXT
        );

        CREATE TABLE IF NOT EXISTS marks (
            mark_id         INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id      TEXT NOT NULL REFERENCES students(student_id),
            semester        INTEGER NOT NULL,
            mathematics     INTEGER NOT NULL,
            physics         INTEGER NOT NULL,
            chemistry       INTEGER NOT NULL,
            english         INTEGER NOT NULL,
            core_subject_1  INTEGER NOT NULL,
            core_subject_2  INTEGER NOT NULL,
            total           INTEGER NOT NULL,
            percentage      REAL NOT NULL,
            result          TEXT NOT NULL
        );
    """)
    conn.commit()
    print("Tables created: students, fees_status, marks")


def generate_students(n=200):
    students = []
    south_indian_cities = [
        ("Chennai", "Tamil Nadu"), ("Coimbatore", "Tamil Nadu"),
        ("Madurai", "Tamil Nadu"), ("Salem", "Tamil Nadu"),
        ("Hyderabad", "Telangana"), ("Warangal", "Telangana"),
        ("Visakhapatnam", "Andhra Pradesh"), ("Vijayawada", "Andhra Pradesh"),
        ("Bengaluru", "Karnataka"), ("Mysuru", "Karnataka"),
        ("Hubballi", "Karnataka"), ("Mangaluru", "Karnataka"),
        ("Kochi", "Kerala"), ("Thiruvananthapuram", "Kerala"),
        ("Kozhikode", "Kerala"), ("Thrissur", "Kerala"),
        ("Puducherry", "Puducherry"),
    ]

    used_emails = set()
    for i in range(1, n + 1):
        first, last = south_indian_name()
        gender = random.choice(["Male", "Female"])
        dept = random.choice(DEPARTMENTS)
        joining_year = random.choice([2021, 2022, 2023, 2024])
        grad_year = joining_year + 4
        city, state = random.choice(south_indian_cities)
        roll = f"{joining_year % 100:02d}{dept[:2].upper()}{i:04d}"
        sid = f"STU{i:05d}"
        dob = fake.date_of_birth(minimum_age=18, maximum_age=25).isoformat()
        address = f"{random.randint(1, 500)}, {fake.street_name()}"

        # ensure unique email
        email = random_email(first, last)
        attempts = 0
        while email in used_emails and attempts < 10:
            email = random_email(first, last)
            attempts += 1
        if email in used_emails:
            email = f"student{i}@college.edu.in"
        used_emails.add(email)

        phone = random_phone()

        students.append({
            "student_id": sid,
            "roll_number": roll,
            "first_name": first,
            "last_name": last,
            "gender": gender,
            "date_of_birth": dob,
            "email": email,
            "phone": phone,
            "address": address,
            "city": city,
            "state": state,
            "department": dept,
            "year_of_joining": joining_year,
            "graduation_year": grad_year,
            "cgpa": None,
        })

    return students


def generate_fees(students):
    records = []
    payment_modes = ["Online", "Cash", "Demand Draft"]
    for s in students:
        semesters_completed = min((2026 - s["year_of_joining"]) * 2, 8)
        semesters_completed = max(semesters_completed, 1)
        total_fee = fee_amount_for_dept(s["department"])

        for sem in range(1, semesters_completed + 1):
            roll = random.random()
            if roll < 0.75:
                paid = total_fee
                status = "Paid"
                pay_date = fake.date_between(start_date="-2y", end_date="today").isoformat()
                mode = random.choice(payment_modes)
            elif roll < 0.90:
                paid = round(random.uniform(0.4, 0.9) * total_fee, 2)
                status = "Partial"
                pay_date = fake.date_between(start_date="-1y", end_date="today").isoformat()
                mode = random.choice(payment_modes)
            else:
                paid = 0.0
                status = "Pending"
                pay_date = None
                mode = None

            records.append({
                "student_id": s["student_id"],
                "semester": sem,
                "total_fee": total_fee,
                "amount_paid": paid,
                "balance": round(total_fee - paid, 2),
                "payment_status": status,
                "payment_date": pay_date,
                "payment_mode": mode,
            })

    return records


def generate_marks(students):
    records = []
    cgpa_map = {}

    for s in students:
        semesters_completed = min((2026 - s["year_of_joining"]) * 2, 8)
        semesters_completed = max(semesters_completed, 1)
        sem_percentages = []

        for sem in range(1, semesters_completed + 1):
            m = random_marks()
            total = sum(m)
            pct = round(total / (len(m) * 100) * 100, 2)
            result = "Pass" if all(x >= 35 for x in m) else "Fail"
            sem_percentages.append(pct)

            records.append({
                "student_id": s["student_id"],
                "semester": sem,
                "mathematics": m[0],
                "physics": m[1],
                "chemistry": m[2],
                "english": m[3],
                "core_subject_1": m[4],
                "core_subject_2": m[5],
                "total": total,
                "percentage": pct,
                "result": result,
            })

        avg_pct = sum(sem_percentages) / len(sem_percentages)
        cgpa_map[s["student_id"]] = round(avg_pct / 10, 2)

    return records, cgpa_map


def insert_students(conn, students, cgpa_map):
    cur = conn.cursor()
    rows = []
    for s in students:
        rows.append((
            s["student_id"], s["roll_number"], s["first_name"], s["last_name"],
            s["gender"], s["date_of_birth"], s["email"], s["phone"],
            s["address"], s["city"], s["state"], s["department"],
            s["year_of_joining"], s["graduation_year"],
            cgpa_map.get(s["student_id"]),
        ))
    cur.executemany(
        "INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows
    )
    conn.commit()
    print(f"Inserted {len(rows)} records into 'students'")


def insert_fees(conn, fees):
    cur = conn.cursor()
    rows = [
        (r["student_id"], r["semester"], r["total_fee"], r["amount_paid"],
         r["balance"], r["payment_status"], r["payment_date"], r["payment_mode"])
        for r in fees
    ]
    cur.executemany("""
        INSERT INTO fees_status
        (student_id, semester, total_fee, amount_paid, balance,
         payment_status, payment_date, payment_mode)
        VALUES (?,?,?,?,?,?,?,?)
    """, rows)
    conn.commit()
    print(f"Inserted {len(rows)} records into 'fees_status'")


def insert_marks(conn, marks):
    cur = conn.cursor()
    rows = [
        (r["student_id"], r["semester"], r["mathematics"], r["physics"],
         r["chemistry"], r["english"], r["core_subject_1"], r["core_subject_2"],
         r["total"], r["percentage"], r["result"])
        for r in marks
    ]
    cur.executemany("""
        INSERT INTO marks
        (student_id, semester, mathematics, physics, chemistry,
         english, core_subject_1, core_subject_2, total, percentage, result)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, rows)
    conn.commit()
    print(f"Inserted {len(rows)} records into 'marks'")


def print_summary(conn):
    cur = conn.cursor()
    print("\n" + "=" * 55)
    print("  DATABASE SUMMARY")
    print("=" * 55)

    for table in ["students", "fees_status", "marks"]:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        count = cur.fetchone()[0]
        print(f"  {table:<20} -> {count:>6} rows")

    print()
    cur.execute("""
        SELECT payment_status, COUNT(*) as cnt
        FROM fees_status
        GROUP BY payment_status ORDER BY cnt DESC
    """)
    print("  Fee payment breakdown:")
    for row in cur.fetchall():
        print(f"    {row[0]:<10} : {row[1]} semesters")

    print()
    cur.execute("""
        SELECT result, COUNT(*) as cnt
        FROM marks GROUP BY result ORDER BY cnt DESC
    """)
    print("  Exam result breakdown:")
    for row in cur.fetchall():
        print(f"    {row[0]:<10} : {row[1]} semesters")

    print()
    cur.execute("""
        SELECT first_name || ' ' || last_name AS name, department, cgpa
        FROM students ORDER BY cgpa DESC LIMIT 5
    """)
    print("  Top 5 students by CGPA:")
    for row in cur.fetchall():
        print(f"    {row[0]:<30} {row[1]:<35} CGPA: {row[2]}")

    print("=" * 55)


def main():
    DB_PATH = "college.db"
    NUM_STUDENTS = 200

    print(f"\nSynthetic College Database Generator")
    print(f"  Students : {NUM_STUDENTS}")
    print(f"  Database : {DB_PATH}\n")

    conn = sqlite3.connect(DB_PATH)
    try:
        create_tables(conn)
        print("Generating data...")
        students = generate_students(NUM_STUDENTS)
        marks_data, cgpa_map = generate_marks(students)
        fees_data = generate_fees(students)

        insert_students(conn, students, cgpa_map)
        insert_fees(conn, fees_data)
        insert_marks(conn, marks_data)

        print_summary(conn)
        print(f"\nDone! Database saved to '{DB_PATH}'")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
