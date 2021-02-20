import vk_api.vk_api
import  random

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

        self.lastCayBoard: VkKeyboard = VkKeyboard(one_time=True)
        self.lastCayBoard.add_button('Привет')

    # Отправка сообщения
    def send_msg(self, send_id:int, message:str, keyList:list=[], anBody:bool = False ):
        """
        :param send_id: id пользователяБ которому отпр. сообщ
        :param message: содержимое отправляемого письма
        """
        #if keyList[len(keyList)-1] == 'Завершить':

        keyboard1: VkKeyboard = VkKeyboard(one_time=True)
        if len(keyList) != 0:
            for i in range(len(keyList)):
                if keyList[i] != '':
                    keyboard1.add_button(keyList[i])
                if i%2==1 and i!=len(keyList)-1:
                    keyboard1.add_line()
            keyboard1.add_line()
            keyboard1.add_button('Сменить режим')
            self.lastCayBoard = keyboard1
        else:
            keyboard1 = self.lastCayBoard

        self.vk_api.messages.send(peer_id=send_id, message=message, random_id=get_random_id(),  keyboard=keyboard1.get_keyboard())




    def start(self):
        # Слушаем сервер
        for event in self.long_poll.listen():
            # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:

                message = event.obj['message']

                peer_id: int = message['peer_id']
                from_id: int = message['from_id']
                text: str = message['text']
                print(message)

                try:
                    action = message['action']
                    if action['type'] == 'chat_invite_user':
                        if from_id != 151819385:
                            self.send_msg(peer_id, 'К нам пришел ' + self.get_user_name(from_id))
                        else:
                            self.send_msg(peer_id, 'Всем привет! Я бот и я хочу играть)')
                    elif action['type'] == 'chat_kick_user':
                        self.send_msg(peer_id, 'Нас покинул  ' + self.get_user_name(from_id))
                except:
                    print('нет action')



                if str(peer_id) not in self.users:
                    self.users[str(peer_id)] = Commander()


                """ Основная инфа"""
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

                if text != '':
                    text = text.strip()#убераем пробелы
                    massageOutput = self.users[str(peer_id)].input(text)
                    # выводим текст
                    self.send_msg(peer_id, massageOutput['txt'], massageOutput['key'], False)





    def get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']