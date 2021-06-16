import json 
import random 

from simpleton import Question

def load_json(path):
        with open("praktyki/062021/maks_grupinski/repo/simpleton/" + path) as file:
            return json.loads(file.read())


questions =  load_json("quiz.json")

questions = [Question(questions[question]) for question in range(len(questions))]

while len(questions) != 0:
    question_id = random.randrange(0, len(questions))
    questions[question_id].question()
    questions[question_id].answers()
    questions[question_id].given_answer()

    del questions[question_id]