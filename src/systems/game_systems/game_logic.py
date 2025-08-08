import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.constants import Constants
from src.systems.relation_systems.embedding_calculator import EmbeddingCalculator

class Game_Logic:
    def __init__(self):
        self.game_state = Constants.GameLogic.GameStates.NOT_STARTED
        self.score = Constants.GameLogic.Defaults.score
        self.embedding_calculator = EmbeddingCalculator()
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
        try: 
             return self.embedding_calculator.calculate_similarity(self.goal, guess)
        except ValueError as e:
            print(f"Error calculating similarity: {e}")
            return None
                
    def get_labels(self):
        # This method should return the labels of the detection model
        # For now, we will return a placeholder list
        if Constants.Game_Settings.release == "demo":
            return Constants.Classes.Demo
        else:
            return Constants.Classes.COCO
    