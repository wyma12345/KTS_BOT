import  random

class Victorina:



    @staticmethod
    def get_victorina_over(text):
        keyList: list = []
        return {'txt': 'Викторина: ввод был: '+text, 'key': keyList}



    @staticmethod
    def get_victorina_questions():
        questions: list = ['вопрос 2','вопрос 3','вопрос 4','вопрос 5','вопрос 6','вопрос 7','вопрос 8']
        #random.shuffle(questions)
        for i in range(len(questions)):
            keyList: list = []
            for k in range(1,5):
                keyList.append('ответ '+str(i+2)+'.'+str(k))
            keyList.append('Завершить')
            yield {'txt': 'МОК Викторина: ' + questions[i], 'key': keyList}



    @staticmethod
    def get_victorina_hello():
        keyList: list = ['ответ 1.1', 'ответ 1.2', 'ответ 1.3', 'ответ 1.4', 'Завершить']
        return {'txt': 'МОК Викторина: Вопрос 1:', 'key': keyList}

    @staticmethod
    def get_victorina_end():
        keyList: list = ['Начать']
        return {'txt': 'МОК Вывод счета:', 'key': keyList}
