import pytest

from app.mechanics import create_questions_list
from app.data import data


def test_create_questions_list():
    # GIVEN questions dict : data
    # WHEN a list [dict  of random questions] is created
    q_list = create_questions_list(data)
    # THEN dict should have ten unique questions
    assert len(q_list) == 10
    assert isinstance(q_list, (list, dict)) is True


def test_populate_round_answers():
    pass
