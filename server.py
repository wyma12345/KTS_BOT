import vk_api.vk_api


from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard

from comand import Commander

class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):

        self.server_name = server_name

        self.vk = vk_api.VkApi(token=api_token)
        self.long_poll = VkBotLongPoll(self.vk, group_id)
        self.vk_api = self.vk.get_api()

        # Словарь дял каждого отдельного пользователя/группы
        self.users = {}
        #self.group = {}#нужно ли

    # Отправка сообщения
    def send_msg(self, send_id, message, keyList:list):
        """
        :param send_id: id пользователяБ которому отпр. сообщ
        :param message: содержимое отправляемого письма
        """

        keyboard1 = VkKeyboard(one_time=True)
        if len(keyList) != 0:
            for i in range(len(keyList)):
                if keyList[i] != '':
                    keyboard1.add_button(keyList[i])
                if i%2==1 and i!=len(keyList)-1:
                    keyboard1.add_line()
            keyboard1.add_line()
        keyboard1.add_button('Сменить режим')

        self.vk_api.messages.send(peer_id=send_id, message=message, random_id=get_random_id(), keyboard=keyboard1.get_keyboard())




    def start(self):
        # Слушаем сервер
        for event in self.long_poll.listen():
            # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:

                message = event.obj['message']

                peer_id: int = message['peer_id']
                from_id: int = message['from_id']
                text: str = message['text']





                if str(peer_id) not in self.users:
                    self.users[str(peer_id)] = Commander()


                """ Основная инфа"""
                print(" ---------- ")
                print(" ---------- ")
                print(" ---------- ")
                print("Тип: ", end="")
                if event.object['message']['id'] > 0:
                    print("private message")

                else:
                    print("group message")
                    if text.count(']'):
                        parts = text.split(']')
                        text = parts[1]
                    #if str(peer_id) not in self.group:
                     #   self.group[str(peer_id)] = Commander()


                print(" ---------- ")
                print("Новое сообщение")
                #print(event.obj['message'])
                print("Имя:" + self.get_user_name(from_id))
                print("Текст:" + text)
                #print(self.vk_api.users.get(user_id=from_id))
                print(" ---------- ")
                """ Основная инфа"""

                text = text.strip()#убераем пробелы


                massageOutput = self.users[str(peer_id)].input(text)
                # выводим текст
                self.send_msg(peer_id, massageOutput['txt'], massageOutput['key'])

                """
                if(text.lower()=='привет'):
                    self.send_msg(peer_id, 'Привет ' +self.get_user_name(from_id) + ' как дела у вашей персоны?')
                elif text.lower()=='инфа':
                    self.send_msg(peer_id, 'Имя: '+self.get_user_name(from_id)+' Город: '+self.get_user_city(from_id))
                elif text.lower()=='хорошо' or text.lower()=='нормально':
                    self.send_msg(peer_id, 'Я рад')
                else:
                    self.send_msg(peer_id, 'К сожалению, я не знаю этой команды :( \n Но Илюша все равно красавчик')
                """





    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']