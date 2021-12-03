import re
from collections import deque
from helper import Helper


class Task3:

    __task_number = 3

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Составить программу циклической перестановки букв в словах текста так, что i-я буква '
              '\nслова становится i+1-ой, а последняя - первой')
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
                text = text.replace(word, self.__shuffle_word(word))
            print(text)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __shuffle_word(word: str) -> str:
        try:
            deque_word = deque(word)
            deque_word.rotate(1)
            return ''.join(deque_word)
        except Exception as e:
            print(f'Ошибка: {e}')
