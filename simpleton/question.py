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
