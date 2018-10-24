import pytest

from app.mechanics import create_questions_list
from app.data import data


def test_create_questions_list():
    q_list = create_questions_list(data)
    assert len(q_list) == 10
