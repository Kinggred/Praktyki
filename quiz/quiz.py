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
        i = 0
        while i < len(self.ans):
            print(str(i+1) + ' ' + self.ans[i])
            i+=1
        print('\n')

    def given_answer(self):
        if self.cor_ans == int(input('Podaj nr odpowiedzi:')):
            print('\nPoprawna odpowiedź')
        else:
            print('\nBłędna odpowiedź')

def load_json(path):
        with open("praktyki/062021/maks_grupinski/repo/quiz/" + path) as f:
            return json.loads(f.read())


questions =  load_json("questions.json")

questions = [Question(questions[question]) for question in range(len(questions))]

while len(questions) != 0:
    q_id = random.randrange(0, len(questions))
    questions[q_id].question()
    questions[q_id].answers()
    questions[q_id].given_answer()

    del questions[q_id]
