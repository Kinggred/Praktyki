import json 
import random 


class Question:
    def __init__(self, dict_load):
        self.qst = dict_load['question']
        self.ans = dict_load['answers']
        self.cor_ans = dict_load['correct_answer']

    def question(self):
        print('\n' + self.qst + '\n')

    def answers(self):
        for answer in range(len(self.ans)):     
            print(str(answer+1) + ' ' + self.ans[answer])

    def given_answer(self):
        if self.cor_ans == int(input('\nPodaj nr odpowiedzi:')):
            print('\nPoprawna odpowiedź')
        else:
            print('\nBłędna odpowiedź')

def load_json(path):
        with open("praktyki/062021/maks_grupinski/repo/quiz/" + path) as file:
            return json.loads(file.read())


questions =  load_json("questions.json")

questions = [Question(questions[question]) for question in range(len(questions))]

while len(questions) != 0:
    question_id = random.randrange(0, len(questions))
    questions[question_id].question()
    questions[question_id].answers()
    questions[question_id].given_answer()

    del questions[question_id]