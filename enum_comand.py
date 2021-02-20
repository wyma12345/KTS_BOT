from enum import Enum
from quest import Quest
from  victorina import Victorina

class CommandQuest(Enum):
    slovo: list = [[Quest.get_quest_up(), 'up', 'вверх'],
             [Quest.get_quest_down(), 'down', 'вниз'],
             [Quest.get_quest_hello(), 'начать']]


class CommandVictorina(Enum):
    #listQuVick = ['вопрос 1','вопрос 2','вопрос 3','вопрос 4','вопрос 5','вопрос 6','вопрос 7']
    gen_iter = Victorina.get_victorina_questions()
    slovo: list = [[next(gen_iter), 'ответ 1.2', 'ответ 1.3','ответ 1.1', 'ответ 1.4','ответ 2.1','ответ 2.2','ответ 2.3','ответ 2.4','ответ 3.1','ответ 3.2','ответ 3.3','ответ 3.4'],
             [Victorina.get_victorina_hello(), 'начать'],
             [Victorina.get_victorina_end(), 'завершить']]