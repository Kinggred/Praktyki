import json as js
import random as rd

#import requests as rq
#r = rq.get('https://raw.githubusercontent.com/Kinggred/Praktyki/quiz/quiz/text.json')

class Quiz:
    def __init__(self):
        self.kt_pyt = -1
        self.bylo = [-1]

    def wgraj_plik(self, ktore, czy_obiekt):
        f = open("praktyki/062021/maks_grupinski/repo/quiz/text.json", "rt")
        q = js.loads(f.read())
        f.close()
        if czy_obiekt != True:
            return q[ktore]
        else:
            return q

    def czy_byl(self, x):
        i = 0
        while i < len(self.bylo)-1:
            if(self.bylo[i] == x):
                return True
            i+=1
        return False

    def l_pyt(self):
        lpyt = rd.randrange(0, len(self.wgraj_plik(0 ,True)))
        if(self.czy_byl(lpyt)):
            while self.czy_byl(lpyt):
                lpyt = rd.randrange(0, len(self.wgraj_plik(0 ,True)))
        self.kt_pyt = lpyt
        self.bylo.append(lpyt)
        return self.kt_pyt

    def zw_wa(self, co_zwr):
        q = self.wgraj_plik(self.kt_pyt, False)
        if co_zwr == 'pyt':
            q = self.wgraj_plik(self.l_pyt(), False)
            return q['question']
        elif co_zwr == 'odp':
            return q['answers']
        elif co_zwr == 'pop':
            return q['correct_answer']

    def zad_pyt(self):
        print(self.zw_wa('pyt') + '\n')
        i = 0
        q = self.zw_wa('odp')
        while i < 4:
            print(str(i+1)+': '+q[i])
            i+=1
        print('\n')

    def psz_odp(self):
        x = int(input('Wprowadź numer odpowiedzi: '))
        y = int(self.zw_wa('pop'))
        if x == y:
            return 'Poprawna Odpowiedź'
        return 'Błędna Odpowiedź'

    def pytanie(self):
        self.zad_pyt()
        print(self.psz_odp())
            


quiz1 = Quiz()

while len(quiz1.bylo) <= len(quiz1.wgraj_plik(0 ,True)):
    quiz1.pytanie()
