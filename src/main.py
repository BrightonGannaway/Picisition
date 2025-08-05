#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from gui.main_gui import Main_GUI
# from systems.game_systems.game_logic import Game_Logic
from src.api.relation_calculator_caller import RelationCalculatorCaller #testing caller implementation



def main():
    # # Initialize the main GUI
    # gui = Main_GUI()
    # # Initialize the game logic
    # gui.run()

    caller = RelationCalculatorCaller()
    input = "bat"
    target = "carrot"
    #caller.model_api.set_System_Prompt("image_game/src/model/system_prompts/model_prompt_3.txtt")
    response = caller.query_relation(input, target, model="relation-calculator")
    print("Response:", response)
    try:
        value = caller.get_relation_value(response)
        print(f"{input} is {int(value * 100)}% related to {target}")
    except ValueError as e:
        print(f"Error processing response: {e}")
    caller.log_response(response, "ran_calclulations.txt")

if __name__ == "__main__":
    main()