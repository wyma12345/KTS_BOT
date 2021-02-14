from enum import Enum
from quest import Quest
from  victorina import Victorina

class CommandQuest(Enum):
    #up = ['up', "вверх"]
    #down = ["down", "вниз"]
    #hello = ['начать']
    slovo: list = [[Quest.get_quest_up(), 'up', 'вверх'],
             [Quest.get_quest_down(), 'down', 'вниз'],
             [Quest.get_quest_hello(), 'начать']]


class CommandVictorina(Enum):
    #yes = ['yes', "да"]
    #no = ["no", "нет"]
    slovo: list = [[Victorina.get_victorina_yes(), 'yes', 'да'],
             [Victorina.get_victorina_no(), 'no', 'нет'],
             [Victorina.get_victorina_hello(), 'начать']]