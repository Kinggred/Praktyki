import pytest

from simpleton import Question

@pytest.fixture()
def dict_load():
    diction = {
       "question": "question",
       "answers": [
           'one',
           'two',
           'three'
       ],
       "correct_answer": 'correct answer'
    }
    return diction

def test_class_returning_proper_values(dict_load):
    quiz = Question(dict_load)
    assert quiz.qst == 'question' and len(quiz.ans) == 3 and quiz.cor_ans == 'correct answer'

