import json
import random

from simpleton.question import Question


def load_json(path):
    with open("/home/user/praktyki/062021/maks_grupinski/repo/simpleton/" +
              path) as file:
        return json.loads(file.read())


questions = load_json("quiz.json")

questions = [
    Question(questions[question]) for question in range(len(questions))
]

while len(questions) != 0:
    question_id = random.randrange(0, len(questions))
    print(questions[question_id].question_text)
    print(questions[question_id].answers)
    if (questions[question_id].given_answer(
            input('Podaj numer odpowiedzi: '))):
        print('Poprawna odpowiedź')
    else:
        print('Błędna odpowiedź')

    del questions[question_id]