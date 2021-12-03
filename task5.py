import re
from collections import deque
from helper import Helper


class Task5:

    __task_number = 5

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текст, содержащий от 2 до 30 слов, в каждом из которых от 2 до 10 латинских букв;'
              '\nмежду соседними словами - не менее одного пробела. Вывести все слова, отличные от последнего'
              '\nслова, предварительно преобразовав каждое из них по следующему правилу:'
              '\n 1) перенести первую букву в конец слова;'
              '\n 2) перенести последнюю букву в начало слова')
        print('----------------------------------------------------------')
        random_text = helper.get_random_text_eng()
        print(random_text)
        print('----------------------------------------------------------')
        self.__print_changed_text(random_text, helper)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __print_changed_text(self, text: str, helper: Helper):
        try:
            list_text = list(re.findall(r"[\w']+", text))
            last_word = list_text[len(list_text) - 1]
            text = text.replace(str(last_word).lower(), '')
            text = text.replace(str(last_word).capitalize(), '')
            words_array = list(set(re.findall(r"[\w']+", text)))
            for word in words_array:
                text = text.replace(word, self.__replace_letters(word, helper))
            print(text)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __replace_letters(word: str, helper: Helper) -> str:
        try:
            deque_word = deque(word)
            deque_word[0], deque_word[len(deque_word) - 1] = helper.swap_letters(
                deque_word[0],
                deque_word[len(deque_word) - 1]
            )
            return ''.join(deque_word)
        except Exception as e:
            print(f'Ошибка: {e}')
