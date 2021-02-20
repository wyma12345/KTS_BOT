# Перечисления команд, режимов
from enum_comand import CommandQuest
from enum_comand import CommandVictorina
from enum_mod import Mode

class Commander:
    from quest import Quest
    from victorina import Victorina

    def __init__(self):

        # Текущий, предыдущий режимы
        self.now_mode = Mode.quest
        self.last_mode = Mode.victorina

    def change_mode(self, to_mode) -> 'None':
        """
        Меняет режим приема команд
        :param to_mode: Измененный мод
        :return: None
        """
        self.last_mode = self.now_mode
        self.now_mode = to_mode

    def input(self, msg: str) -> dict:
        """
        Функция принимающая сообщения пользователя
        :param msg: Сообщение
        :return: Ответ пользователю, отправившему сообщение
        """

        # Проверка на команду смены мода
        # Если была команда "Сменить вид"
        if msg.lower() == 'сменить режим':
            self.change_mode(self.last_mode)
            return {'txt': "Режим изменен на " + self.now_mode.value[0], 'key': ['Начать']}

        # Если команда смены начиналась с "/"
        if msg.startswith("/"):
            for mode in Mode:
                if msg.split('/')[1] in mode.value:
                    self.change_mode(mode)
                    return {'txt': "Режим изменен на " + self.now_mode.value[0], 'key': ['Начать']}
            return {'txt': "Неизвестный мод " + msg.split('/')[1], 'key': []}


        # Команды для квеста
        if self.now_mode == Mode.quest:
            for i in CommandQuest.slovo.value:
                if msg.lower() in i:
                    return i[0]
            else:
                return self.Quest.get_quest_over(msg)

            """
            if msg.lower() in CommandQuest.up.value:
                return self.Quest.get_quest_up()
            elif msg.lower() in CommandQuest.down.value:
                return self.Quest.get_quest_down()
            elif msg.lower() in CommandQuest.hello.value:
                return self.Quest.get_quest_hello()
            else:
                return self.Quest.get_quest_over(msg)
            """


        # Команды для викторины
        elif self.now_mode == Mode.victorina:
            for i in CommandVictorina.slovo.value:
                if msg.lower() in i:
                    return i[0]
            else:
                return self.Victorina.get_victorina_over(msg)

            """
                        if msg.lower() in CommandVictorina.yes.value:
                return self.Victorina.get_victorina_yes()
            elif msg.lower() in CommandVictorina.no.value:
                return self.Victorina.get_victorina_no()
            else:
                return self.Victorina.get_victorina_over(msg)
            """
