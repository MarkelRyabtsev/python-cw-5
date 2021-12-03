import re
from collections import deque
from helper import Helper


class Task4:

    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('В каждом слове текста замените "а" на букву "е", если "а" стоит на четном месте, и заменить '
              '\nбукву "б" на сочетание "ак", если "б" стоит на нечетном месте')
        print('----------------------------------------------------------')
        random_text = helper.get_random_text()
        print(random_text)
        print('----------------------------------------------------------')
        self.__print_shuffled_text(random_text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __print_shuffled_text(self, text: str):
        try:
            words_array = list(set(re.findall(r"[\w']+", text)))
            for word in words_array:
                text = text.replace(word, self.__replace_even_letter(word, 'а', 'е'))
                text = text.replace(word, self.__replace_odd_letter(word, 'б', 'ак'))
            print(text)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __replace_even_letter(word: str, old: str, new: str) -> str:
        try:
            deque_word = deque(word)
            for i in range(0, len(word) - 1):
                if (i + 1) % 2 == 0 and deque_word[i] == old:
                    deque_word[i] = new
            return ''.join(deque_word)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __replace_odd_letter(word: str, old: str, new: str) -> str:
        try:
            deque_word = deque(word)
            for i in range(0, len(word) - 1):
                if (i + 1) % 2 != 0 and deque_word[i] == old:
                    deque_word[i] = new
            return ''.join(deque_word)
        except Exception as e:
            print(f'Ошибка: {e}')
