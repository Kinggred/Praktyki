import pytest

from simpleton.question import Question


@pytest.fixture()
def dict_load():
    diction = {
        "question": "question",
        "answers": ['one', 'two', 'three'],
        "correct_answer": 1
    }
    return diction


def test_class_returning_proper_values(dict_load):
    quiz = Question(dict_load)
    assert quiz.question_text == '\n' + 'question'
    assert len(quiz.ans) == 3
    assert quiz.cor_ans == 1


def test_does_function_check_values_properly(dict_load):
    quiz = Question(dict_load)
    assert quiz.given_answer(1)
    assert not quiz.given_answer(2)


def test_does_function_return_proper_answers_string(dict_load):
    quiz = Question(dict_load)
    assert quiz.answers == '\n1 one\n2 two\n3 three\n'