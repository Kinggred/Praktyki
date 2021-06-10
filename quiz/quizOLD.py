import json as js
import random as rd


class FileLoader:
    def __init__(self):
        self.jsn
        
    def load_from_json(self, json_location, open_type):
        try:
            file = open(json_location, open_type)
            self.jsn = js.loads(file.read())
            file.close()
        except:
            print('Błąd Pliku')

    def file_return(self, not_list, dict_num):
        if not_list:
            return self.jsn
        else:
            return self.jsn[dict_num]
    
    def get_file_length(self):
        return len(self.jsn)


class Question_Loader:
    def __init__(self):
        self.qst_id = -1
        self.used = [-1]

    def get_rand_qst(self, file_length):
        rand_qst_num = rd.randrange(0, file_length)

        if(self.was_used(rand_qst_num)):
            while self.was_used(rand_qst_num):
                rand_qst_num = rd.randrange(0, len(self.file_load(0 ,True)))

        self.qst_id = rand_qst_num
        self.used.append(rand_qst_num)
        return self.qst_id

    def was_used(self, num):
        i = 0
        while i < len(self.used)-1:
            if(self.used[i] == num):
                return True
            i+=1
        return False


class Question_data:
    def __init__(self, file):
        self.file = file
        self.q = self.file
    def get(self, what_to_return):
        if what_to_return == 'pyt':
            self.q = self.file
            return self.q['question']
        elif what_to_return == 'odp':
            return self.q['answers']
        elif what_to_return == 'pop':
            return self.q['correct_answer']


file_ini = FileLoader()
file = file_ini.load_from_json('praktyki/062021/maks_grupinski/repo/quiz/text.json', 'rt')

i = 0
while i > file_ini.get_file_length:
    question = Question_Loader().get_rand_qst(file.get_file_length)
    qst_data = Question_data(file.jsn[question])

