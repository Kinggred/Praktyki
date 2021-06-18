class Question:
    def __init__(self, dict_load):
        self.question_text = '\n' + dict_load['question']
        self.ans = dict_load['answers']
        self.cor_ans = dict_load['correct_answer']
        self.answers_text = '\n'

    @property
    def answers(self):
        for answer in range(len(self.ans)):
            self.answers_text += str(answer +
                                     1) + ' ' + self.ans[answer] + '\n'
        return self.answers_text

    def given_answer(self):
        if self.cor_ans == int(input('Podaj nr odpowiedzi:')):
            print('\nPoprawna odpowiedź')
        else:
            print('\nBłędna odpowiedź')
