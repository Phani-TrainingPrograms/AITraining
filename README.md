# AITraining
Demos on AI and Agentic AI  

### Software to be installed
1. Python 26.x and the scripts added to the Path Environment Variable.
2. Antigravity or VS code IDE.
3. Install pip if not available.

    
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
9. Update the changes with the code from the shared Ex01.py
10. Set the generated API Key from step 2 to the variable called api_key.
    ```
    api_key="UR_API_KEY",
    ``` 
11. Save the file and run the following command to execute the python script.
    ```
    py scriptName.py
    ```        


