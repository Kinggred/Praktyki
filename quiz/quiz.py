import json as js
import random as rd

class File_load():
    def load_json(self, path, type_of):
        f = open(path, type_of)
        q = js.loads(f.read())
        f.close()
        return q

class Question:
    def __init__(self, dict_load):
        self.dict = dict_load
        self.qst = self.dict['question']
        self.ans = self.dict['answers']
        self.cor_ans = self.dict['correct_answer']

    def was_ans_cor(self, ans_nr):
        if self.cor_ans == ans_nr:
            return True

class Quiz:
    def get_qst(self, range):
        return rd.randrange(0, len(range))



q = File_load().load_json("praktyki/062021/maks_grupinski/repo/quiz/text.json", "rt")
questions = q
qz = Quiz()
i = 0

while i < len(questions):
    questions[i] = Question(q[i])
    i+=1

while len(questions) != 0:
    q_id = qz.get_qst(questions)
    print('\n' + questions[q_id].qst + '\n')
    i = 0
    while i < len(questions[q_id].ans):
        print(str(i+1) + ' ' + questions[q_id].ans[i])
        i+=1
    print('\n')

    if questions[q_id].was_ans_cor(int(input('Podaj nr odpowiedzi:'))):
        print('\nPoprawna odpowiedź')
    else:
        print('\nBłędna odpowiedź')

    del questions[q_id]
