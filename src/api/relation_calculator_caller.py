import os
import sys
from src.api.model_api import Model_API

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class RelationCalculatorCaller:
    def __init__(self):
        self.model_api = Model_API()
        self.model_api.set_System_Prompt("image_game/src/model/system_prompts/model_prompt.txt")


    def query_relation(self, input: str, target: str, model="relation-calculatorlatest",):
        response = self.model_api.query(model="relation-calculatorlatest", msg=f"<in> {input} </in> <tar> {target} </tar>")
        return response
    
    def get_relation_value(self, response):
        if isinstance(response, dict) and "choices" in response and len(response["choices"]) > 0:
            content = response["choices"][0]["message"]["content"]
            start = content.find("<rel>") + len("<rel>")
            end = content.find("</rel>")
            value_str = content[start:end].strip()
            print(response, "\n\n\n")
            print(value_str)
            value = float(value_str)
            return value
        else:
            raise ValueError(f"Invalid response format: {response}")

    def log_response(self, response, filename="debug.txt"):
        with open(filename, "w") as file:
            file.write(str(response))