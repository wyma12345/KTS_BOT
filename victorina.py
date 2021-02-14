class Victorina:
    @staticmethod
    def get_victorina_over(text) -> dict:
        keyList: list = ['Абсолютно да', 'Абсолютно нет', 'Сомнительно да', 'Сомнительно нет']
        return {'txt': 'Викторина: ввод был: '+text, 'key': keyList}

    @staticmethod
    def get_victorina_yes() -> dict:
        keyList: list = ['да1', 'да2']
        return {'txt': 'Викторина: ввод да', 'key': keyList}

    @staticmethod
    def get_victorina_no() -> dict:
        keyList: list = ['нет1', 'нет2']
        return {'txt': 'Викторина: ввод нет', 'key': keyList}

    @staticmethod
    def get_victorina_hello() -> dict:
        keyList: list = ['да', 'нет', '1', '2', '3']
        return {'txt': 'Выберите команду для викторины:', 'key': keyList}
