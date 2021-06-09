import json as js
import random as rd


class Quiz:
    def __init__(self):
        self.qst_id = -1
        self.used = [-1]

    def file_load(self, num, not_list):
        f = open("praktyki/062021/maks_grupinski/repo/quiz/text.json", "rt")
        q = js.loads(f.read())
        f.close()
        if not_list != True:
            return q[num]
        else:
            return q

    def was_used(self, num):
        i = 0
        while i < len(self.used)-1:
            if(self.used[i] == num):
                return True
            i+=1
        return False

    def get_rand_question(self):
        rnd_qst = rd.randrange(0, len(self.file_load(0 ,True)))
        if(self.was_used(rnd_qst)):
            while self.was_used(rnd_qst):
                rnd_qst = rd.randrange(0, len(self.file_load(0 ,True)))
        self.qst_id = rnd_qst
        self.used.append(rnd_qst)
        return self.qst_id

    def get_qst_data(self, what_to_return):
        q = self.file_load(self.qst_id, False)
        if what_to_return == 'pyt':
            q = self.file_load(self.get_rand_question(), False)
            return q['question']
        elif what_to_return == 'odp':
            return q['answers']
        elif what_to_return == 'pop':
            return q['correct_answer']

    def ask_question(self):
        print(self.get_qst_data('pyt') + '\n')
        i = 0
        q = self.get_qst_data('odp')
        while i < int(len(self.get_qst_data('odp'))):
            print(str(i+1)+': '+q[i])
            i+=1
        print('\n')

    def get_answer(self):
        i = input('Wprowadź numer odpowiedzi: ')
        y = self.get_qst_data('pop')
        while i > str(len(self.get_qst_data('odp'))) or i == None:
            i = int(input('Wprowadź numer odpowiedzi: '))
        if i == y:
            return 'Poprawna Odpowiedź'

        return 'Błędna Odpowiedź'

    def start(self):
        self.ask_question()
        print(self.get_answer())
            


quiz1 = Quiz()

while len(quiz1.used) <= len(quiz1.file_load(0, True)):
    quiz1.start()
