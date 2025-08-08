# game runner handels the juggling of game state, logic and gui in order to organize the game flow 
# within the program environment

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.systems.game_systems.game_logic import Game_Logic

class Game_Runner:
    def __init__(self):
        self.game_logic = Game_Logic()

    def run(self):
        self.game_logic.set_random_goal()
        self.game_logic.start_game()
        print(f"Game started with goal: {self.game_logic.goal}")

    def new_game(self):
        self.game_logic.set_random_goal()
        print(f"New game started with goal: {self.game_logic.goal}")

    def check_win_condition(self, guess):
        return self.game_logic.check_guess(guess)

    def relate_guess_to_goal(self, guess):
        if self.game_logic.check_guess(guess):
            return 1.0  # 100% related
        else:
            return self.game_logic.get_analysis_result(guess)