"""
This module is to get data from api and return the question list
"""

import requests


class Generate:

    def __init__(self, difficulty, question_type):
        self.difficulty = difficulty.lower()
        self.question_type = question_type.lower()
        self.question_list = []

    # Convert question according to the user difficulty
    def get_difficulty(self):
        if self.difficulty == '1' or self.difficulty == 'easy':
            return 8
        elif self.difficulty == '2' or self.difficulty == 'hard':
            return 16
        else:
            return 24

    # Convert question type according to user
    def get_question_type(self):
        if self.question_type == '1':
            return 'boolean'
        if self.question_type == '2':
            return 'multiple'

    # Generate question from api
    def get_data(self):
        request = requests.get(
            f"https://opentdb.com/api.php?amount={self.get_difficulty()}&type={self.get_question_type()}")

        data = request.json()['results']
        return data

