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

    
class Rng:
    def get_qst(self, range):
        return rd.randrange(0, len(range))


class Quiz:
    def __init__(self):
        pass
    
    def question(self, question):
        print('\n' + question + '\n')

    def answers(self, answers):
        i = 0
        while i < len(answers):
            print(str(i+1) + ' ' + answers[i])
            i+=1
        print('\n')

    def answer(self, cor_ans):
        if self.was_ans_cor(cor_ans, int(input('Podaj nr odpowiedzi:'))):
            print('\nPoprawna odpowiedź')
        else:
            print('\nBłędna odpowiedź')

    def was_ans_cor(self, cor_ans, ans_nr):
        if cor_ans == ans_nr:
            return True


q = File_load().load_json("praktyki/062021/maks_grupinski/repo/quiz/text.json", "rt")
questions = q
rng = Rng()
quiz = Quiz()
i = 0

while i < len(questions):
    questions[i] = Question(q[i])
    i+=1

while len(questions) != 0:
    q_id = rng.get_qst(questions)
    quiz.question(questions[q_id].qst)
    quiz.answers(questions[q_id].ans, )
    quiz.answer(questions[q_id].cor_ans)

    del questions[q_id]
