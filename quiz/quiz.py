import json 
import random 


class Question:
    def __init__(self, dict_load):
        self.dict = dict_load
        self.qst = self.dict['question']
        self.ans = self.dict['answers']
        self.cor_ans = self.dict['correct_answer']

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


def load_json(path, type_of):
        f = open(path, type_of)
        q = json.loads(f.read())
        f.close()
        return q


questions_js =  load_json("praktyki/062021/maks_grupinski/repo/quiz/text.json", "rt")

questions = [Question(questions_js[question]) for question in range(len(questions_js))]

while len(questions) != 0:
    q_id = random.randrange(0, len(questions))
    questions[q_id].question()
    questions[q_id].answers()
    questions[q_id].given_answer()

    del questions[q_id]
