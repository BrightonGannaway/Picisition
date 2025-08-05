import requests
from dotenv import load_dotenv
import os
import json
import sys
import constants


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
class Model_API:
    def __init__(self):
        self.model_prompt = ""

    # result = query_model("<in> apple </in> <tar> orange </tar>")
    # print(result)


    # /(<in> ?[a-zA-Z ]+ ?<\/in> <tar> ?[a-zA-Z ]+ ?<\/tar>){1}/gm
    # regex for our format 
    # This function queries the model API for a relation calculation
    def query(self, model: str, msg: str, stream=False):
        print("querying model: ", model)
        load_dotenv()
        API_KEY = os.getenv("WEBUI-KEY")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        print("message: ", msg)
        #print("system prompt: ", self.model_prompt)
        payload = {
            "model": model,
            "temperature": constants.Constants.ModelAPI.Defaults.temperature,
            "top_p": constants.Constants.ModelAPI.Defaults.top_p,
            "max_tokens": constants.Constants.ModelAPI.Defaults.max_tokens,
            "stop": constants.Constants.ModelAPI.Defaults.stop_sequences,
            "messages": [
                {"role": "system", "content": self.model_prompt},
                {"role": "user", "content": msg}
            ],
            "stream": stream
            
        }

        print("attempting query")
        resp = requests.post(
            "http://localhost:8080/api/chat/completions",
            headers=headers,
            json=payload
        )

        return resp.json() if not stream else resp.iter_lines()


    #access the first item of choices to access the content of a message
    # content = resp["choices"][0]["message"]["content"]
    # start = content.find("<rel>") + len("<rel>")
    # end = content.find("</rel>")
    # value_str = content[start:end].strip()
    # print(resp, "\n\n\n")
    # print(value_str)
    # value = float(value_str)
    # print(f"{input} is {int(value * 100)}% related to {target}")

    def set_System_Prompt(self, filename: str):
        with open(filename, "r") as file:
            self.model_prompt = file.read().strip()
            print("Setting prompt set to:", self.model_prompt)