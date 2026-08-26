# AITraining
Demos on AI and Agentic AI  

### Software to be installed
1. Python 26.x from https://www.python.org/downloads/ and add Python to the Path Environment Variable.
2. Antigravity from https://edgedl.me.gvt1.com/edgedl/release2/j0qc3/antigravity/stable/2.5.5-4923483625488384/windows-x64/Antigravity%20IDE.exe.
3. Alternatively you can also use Cursor instead of Antigravity as your IDE.
4. Install pip if not available.

    
### Steps for creating a AI Project.
1. Open the Google AI studio from this link: https://aistudio.google.com/welcome?utm_source=google&utm_medium=cpc&utm_campaign=Cloud-SS-DR-AIS-FY26-global-gsem-1713578&utm_content=text-ad&utm_term=KW_google%20ai%20studio&gad_source=1&gad_campaignid=23417416052&gbraid=0AAAAACn9t647Qm7FL9yGpuwRhaa-ySbYj&gclid=Cj0KCQjwnbrUBhDOARIsAKKhPpccN7ldwTqVRBXCiusvaqXNUQkypHSS5mZZ-5pkN8oW-qplABYg5IQaAkWIEALw_wcB
2. Click on Get started and accept the End User licence and other options which shall redirect to the below screen.
   <img width="1897" height="897" alt="image" src="https://github.com/user-attachments/assets/4a7d48e7-dd33-49b1-876c-973b9882a880" />

3. Create a new project in the Google AI Studio.
4. Generate a new key for that project. Keep it safe and use it in a secured manner.
5. In the AI Studio, search for Model selection.
6. Choose Gemini 3.5 Flash Lite Model. Models are patterns that are well tested/trained and consumed by programmers for building AI Strategies.
7. Click on GetCode Tab beside the selected Model and copy it to clipboard.
8. Create a new folder in your fav IDE (VS Code, Antigravity).  
9. Paste the copied code into a py script file.
10. Use the below command to install google genai
   ```
    py -m pip install google-genai
   ```
11. Update the changes with the code from the shared Ex01.py.
12. In the contents section, update the text property with the prompt(Question) that you want the AI to respond.
<img width="571" height="257" alt="image" src="https://github.com/user-attachments/assets/02a73200-5782-4f54-9480-8df33580397b" />
      
13. Set the generated API Key from step 2 to the variable called api_key.
    ```
    api_key="UR_API_KEY",
    ``` 
14. Save the file and run the following command to execute the python script.
    ```
    py scriptName.py
    ```
    -------------------------------------------------------------------------------------------------------------------------------------------------------------
    ## Exercise 2
    ### Using .env file without hardcoding the API Key and the prompt and create Interactive Console

    1. Create a new file called .env and place the content as shared in the .env file.
    2. Replace the API Key with your generated key.
    3. Create a new text file called Prompt_Ex02.txt which contains the prompt that we want the AI tool to generate the required infrastructure for the desired result.
    4. Any prompt follows TASK, CONTEXTS, REFERENCES, EVALUATE and ITERATE.
    5. Use this pattern for creating new prompts instead of hard coding it in the Text block of the python file.
    6. Sample Prompt is shared and refer SampleProj\prompt_ex02.txt.
    7. Open the AntiGravity ChatBot and drag the prompt_ex02.txt into the ChatBot and type review and implement

        <img width="354" height="52" alt="image" src="https://github.com/user-attachments/assets/5cb17ff3-b12c-4bbf-92a5-588aec635e56" />
    8. Allow the Antigravity agent to review the prompt and allow it to make changes to the existing code. Accept the changes. 
    9. After saving the file, run the python script as we did previously in step 13 of the previous exercise. Dont forget to change the filename.
    10. Notice that the terminal shall now be user responsive and waits for you to ask a Prompt for which it answers accordingly.

## Exercise 3
### To create User Interface for chat bot using tkinter.
1. Design the User interface required for the chat bot using draw.io or Paint Application and save it as ui.png. A snap shot of it is shared below
<img width="422" height="390" alt="image" src="https://github.com/user-attachments/assets/17606b49-11db-40e8-93d8-5f6821ef7910" />


2. Create a new file called Ex03.py and copy the contents of Ex02.py into it. This file shall be modified by Antigravity chatbot based on the inputs we provide to generate the User interface. 
3. Create a new file called prompt_Ex03.txt which shall contain the prompt that allows to create an User interface for our existing Chat Bot. 
4. Copy the contents of the SampleProj\prompt_Ex03.txt that is shared in the Repo. 
5. Make sure to modify the paths of the ui.png as per your file location. 
6. Open the AntiGravity ChatBot and drag the prompt_ex03.txt into the ChatBot and type review and implement -> You should perform this step whenever you want AntiGravity ChatBot to respond and generate the required code for your Application. 
7. Antigravity Chat bot shall modify the contents of Ex03.py to suit our requirement. 
8. Antigravity shall also generate ui.py that shall contain the code for UI. 
9. Run the ui.py to see the desired output: The UI shall be displayed, allowing the user to chat and get responses.
10. The ui.py and generated files from the Prompt will not be available in the repo, this will generated when you execute the commands using prompt.txt


## Exercise 4
### To create a function calling  to a json db to get data
### What is Function calling?
Function calling in AI is the mechanism that lets a language model (like GPT) invoke external tools, APIs, or code functions by outputting structured requests (usually JSON), enabling the model to go beyond text generation and actually perform actions such as fetching data, running computations, or interacting with applications. Simply put : Function calling is the bridge between reasoning and action in AI. It lets models not just talk about the world but interact with it—fetching live data, running code, or automating workflows.
| Aspect | Plain Text Generation | Function Calling |
| --- | --- | --- |
| Output Format | Free-form text | Structured JSON/tool call |
| Capabilities | Language only | Language + external actions |
| Example Use | “It’s usually warm in Bengaluru.” | Calls weather API → “It’s 28°C in Bengaluru right now.” |
| Applications | Chatbots, writing | AI agents, automation, workflows |


Steps:
1. Create a JSON file that contains sample data for a vegetable vendor which has a collection of Vegetables/Fruits with attributes Name, Type, Price. A Sample JSON file is shared. You can use the same file as your datasource.        
2. Create a new file called Ex04.py and copy the contents of Ex03.py into it. This file shall be refered by Antigravity chatbot based on the inputs we provide to generate the User interface. 
3. Create a new file called prompt_Ex04.txt which shall contain the prompt that allows to create an User interface for our existing Chat Bot. 
4. Copy the contents of the SampleProj\prompt_Ex04.txt that is shared in the Repo. 
5. Make sure to modify the path of the JSON File database.json as per your file location in the prompt_Ex04.txt. 
6. Open the AntiGravity ChatBot and drag the prompt_ex04.txt into the ChatBot and type review and implement -> You should perform this step whenever you want AntiGravity ChatBot to respond and generate the required code for your Application. 
7. Antigravity Chat bot shall modify the contents of Ex04.py to suit our requirement based on the inputs we have mentioned in the prompt. 
8. Antigravity shall generate the following files :
    a. ui.py that shall contain the code for UI and adds the button for loading System prompt and reset chat. This is the updation from the previous example. 
    b. Tooling.py will contain the all the APIs and Functions required for extracting the information.
    c. system_prompt.txt defines the role of the AI function calling assistant for querying grocery items and pricing.  
9. Run the ui.py to see the desired output: The UI shall be displayed, allowing the user to chat and get responses.
10. Click on load System prompt that facilitates the UI to take the database.json and get the desired results.

<img width="760" height="433" alt="image" src="https://github.com/user-attachments/assets/bb376e47-b649-4662-b49a-341b8eb278e5" />


## Exercise 5
### To use SQLite database to create an MCP server and implement Chatbot.

#### What is MCP?
- MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems.
- Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks. Consider MCP as a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

#### Architecture of MCP
Refer the below document for more details:
https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
<img width="1650" height="644" alt="image" src="https://github.com/user-attachments/assets/514f624d-172c-4345-9d61-41f9e8d8c81f" />

#### Steps:
1. Create a new file called synth_data.txt and copy the contents from the shared file in the repo. 
2. Drag the file into the Antigravity chatbot and append it with review and implement. 
3. Antigravity shall generate the required databases into the containing folder. It uses faker to generate the data required for the databases.
4. You should use the below script to install faker extension into the system. 
```
    py -m pip install faker
```
5. Add a new extension SqlLite Viewer to view the generated database and its data from the Antigravity. 
<img width="243" height="181" alt="image" src="https://github.com/user-attachments/assets/6ce209f4-dc53-4c90-87ee-4154279cdacf" />

6. The Chatbot shall generate the following files:
   
    a. college.db ->The SQLLite database that contains the data for our chatbot.
    
    b. synth_data.py -> The script for extracting the data from the SQLLite. 
8. Create a new file called question_prompt.txt and copy the contents from the question_prompt.txt in the repo.
9. Drag the question_prompt.txt into the Antigravity chatbot and answer the relavent questions raised by the chatbot.

```
NOTE: This questionaire is more like a Congitive Verifier Technique  which provides a platform for discussion with the expert. 
```     
9. After all the questions are answered, ask the Chatbot to generate the required files. 
10. This shall update the tooling.py.
11. Run the tooling.py in a separate terminal.
12. Using prompt_mcp.txt, ask the AntiGravity chatbot to review and implement.
13. Run this prompt to allow Antigravity to modify the system_prompt to use the DB as the data source
    ```
    [Ex05.py](file;file:///c%3A/Trainings/AI%20training/SampleProj/Ex05.py) Review and implement with reference to [tooling.py](file;file:///c%3A/Trainings/AI%20training/SampleProj/tooling.py) 
    ```
14. Apply the changes and run the Ex05.py in a separate Terminal.
15. If any errors are displayed, ask the ChatBot to fix it and it fixes accordingly. 
NOTE: You may have to restart the IDE to view the MCP server that U have created. U should relaunch the tooling.py and click on refresh button.
 <img width="636" height="512" alt="image" src="https://github.com/user-attachments/assets/a366ccde-5b36-4ec8-9052-b94b0425c04e" />

