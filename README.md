# AITraining
Demos on AI and Agentic AI  

### Software to be installed
1. Python 26.x from https://www.python.org/downloads/ and add Python to the Path Environment Variable.
2. Antigravity from https://edgedl.me.gvt1.com/edgedl/release2/j0qc3/antigravity/stable/2.5.5-4923483625488384/windows-x64/Antigravity%20IDE.exe.
3. Alternatively you can also use Cursor instead of Antigravity as your IDE.
4. Install pip if not available.

    
### Steps for creating a AI Project.
1. Create a new project in the Google AI Studio.
2. Generate a new key for that project. Keep it safe and use it in a secured manner.
3. In the AI Studio, search for Model selection.
4. Choose Gemini 3.5 Flash Lite Model. Models are patterns that are well tested/trained and consumed by programmers for building AI Strategies.
5. Click on GetCode Tab beside the selected Model and copy it to clipboard.
6. Create a new folder in your fav IDE (VS Code, Antigravity).  
7. Paste the copied code into a py script file.
8. Use the below command to install google genai
   ```
    py -m pip install google-genai
   ```
9. Update the changes with the code from the shared Ex01.py.
10. In the contents section, update the text property with the prompt(Question) that you want the AI to respond.
<img width="571" height="257" alt="image" src="https://github.com/user-attachments/assets/02a73200-5782-4f54-9480-8df33580397b" />
      
12. Set the generated API Key from step 2 to the variable called api_key.
    ```
    api_key="UR_API_KEY",
    ``` 
13. Save the file and run the following command to execute the python script.
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
<img width="822" height="690" alt="image" src="https://github.com/user-attachments/assets/17606b49-11db-40e8-93d8-5f6821ef7910" />


2. Create a new file called Ex03.py and copy the contents of Ex02.py into it. This file shall be modified by Antigravity chatbot based on the inputs we provide to generate the User interface. 
3. Create a new file called prompt_Ex03.txt which shall contain the prompt that allows to create an User interface for our existing Chat Bot. 
4. Copy the contents of the SampleProj\prompt_Ex03.txt that is shared in the Repo. 
5. Make sure to modify the paths of the ui.png as per your file location. 
6. Open the AntiGravity ChatBot and drag the prompt_ex03.txt into the ChatBot and type review and implement -> You should perform this step whenever you want AntiGravity ChatBot to respond and generate the required code for your Application. 
7. Antigravity Chat bot shall modify the contents of Ex03.py to suit our requirement. 
8. Antigravity shall also generate ui.py that shall contain the code for UI. 
9. Run the ui.py to see the desired output: The UI shall be displayed, allowing the user to chat and get responses. 

    
             


