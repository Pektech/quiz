from app.data import data
from random import choices

myth_questions = data


SCORE = 0
Q_COUNT = 0
NUM_OF_QUESTIONS = 10


# print list of NUM_OF_QUESTIONS


def create_questions_list(data):
    """create a random list of set length from the data questions"""
    questions_list = choices(myth_questions, k=NUM_OF_QUESTIONS)
    return questions_list
