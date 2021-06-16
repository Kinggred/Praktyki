import pytest
import json

@pytest.fixture()
def json_file():
    with open("praktyki/062021/maks_grupinski/repo/simpleton/quiz.json") as file:
            return json.loads(file.read())

@pytest.fixture()
def json_lenght(json_file):
    return range(len(json_file))

def test_every_element_has_question(json_file, json_lenght):
    check = False
    for question in json_lenght:
        file = json_file[question]
        file = file['question']
        if file == None or  file[-1] == "":
            check = True
    assert check == False

def test_every_element_has_answers(json_file, json_lenght):
    check = False
    for answer in json_lenght:
        file = json_file[answer]
        file = file['answers']
        if file[0] == None:
            check = True
    assert check == False

def test_every_element_has_correct_answer(json_file, json_lenght):
    check = False
    for cor_answer in json_lenght:
        file = json_file[cor_answer]
        if file['correct_answer'] == None:
            check = True
    assert check == False or None

def test_correct_answer_has_corresponding_answer(json_file, json_lenght):
    check = False
    for cor_answer in json_lenght:
        file = json_file[cor_answer]
        amound_of_options = len(file['answers'])
        if not file['correct_answer'] <= amound_of_options or file['correct_answer'] == 0:
            check = True
    assert check == False or None

