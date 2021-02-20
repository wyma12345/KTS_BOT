class Quest:
    @staticmethod
    def get_quest_up() -> dict:
        keyList:list = ['вверх1', 'вверх2']
        return {'txt': 'Квест: ввод вверх', 'key': keyList, 'body': True}

    @staticmethod
    def get_quest_down() -> dict:
        keyList: list = ['вниз1', 'вниз2']
        return {'txt': 'Квест: ввод вниз', 'key': keyList}

    @staticmethod
    def get_quest_over(text) -> dict:
        keyList: list = ['вверх', 'вниз', 'право', 'лево']
        return {'txt': 'Квест: ввод был:' + text, 'key': keyList}

    @staticmethod
    def get_quest_hello() -> dict:
        keyList: list = ['вверх', 'вниз', '1', '2', '3']
        return {'txt': 'Выберите команду для квеста:', 'key': keyList}