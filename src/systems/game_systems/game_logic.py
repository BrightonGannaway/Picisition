import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.api.relation_calculator_caller import RelationCalculatorCaller
from src.constants import Constants

class Game_Logic:
    def __init__(self):
        self.game_state = Constants.GameLogic.GameStates.NOT_STARTED
        self.score = Constants.GameLogic.Defaults.score
        self.caller = RelationCalculatorCaller()
        self.goal = "" #daily object player has to find with detection model
        self.guesses = [] #list of guesses player has made
        self.closest_guess = None #closest guess to the goal, implement later for precentage similarity

    def start_game(self):
        self.game_state = Constants.GameLogic.GameStates.IN_PROGRESS


    def set_goal(self, goal):
        self.goal = goal
    
    #used for the daily goal, will implement something a bit more complex later
    def set_random_goal(self):
        import random
        goal = random.choice(self.get_labels())
        self.set_goal(goal)

    def check_guess(self, guess):

        self.guesses.append(guess)
        return guess == self.goal

    def get_analysis_result(self, guess):
        guesses = []

        #we check if the guess is already in the database with the target if so we return tbe relation value
        with open(Constants.GameLogic.files.ran_calculations, "r", encoding='utf-8') as file:     
            for line in file:
                if line[line.find("<in>") + len("</in>"):line.find("</in>")].strip() == guess and line[line.find("<tar>") + len("<tar>"):line.find("</tar>")].strip() == self.goal:
                    return float(line[line.find("<rel>") + len("<rel>"):line.find("</rel>")].strip())
                
        #else we use the relation calculator to get the relation value
        response = self.caller.query_relation(guess, self.goal, model="relation-calculatorlatest")
        value = self.caller.get_relation_value(response)
        self.caller.log_response(response, "image_game/db/ran_calculations.txt")

    def get_labels(self):
        # This method should return the labels of the detection model
        # For now, we will return a placeholder list
        return ["tv", "laptop", "person"]
    