import random
import re

from helper import Helper


class Task16:

    __task_number = 16

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны два числа: N1 и N2, и две строки: s1 и s2. Получить из этих строк новую строку, '
              '\nобъединив N1 первых символов строки s1 и N2 последних символов строки s2')
        print('----------------------------------------------------------')
        n1 = random.randint(1, 5)
        n2 = random.randint(1, 5)
        random_text_1 = helper.get_random_short_text_eng()
        random_text_2 = helper.get_random_short_text_eng()
        print(f'N1: {n1}   N2: {n2}')
        print('----------------------------------------------------------')
        print(random_text_1)
        print('----------------------------------------------------------')
        print(random_text_2)
        print('----------------------------------------------------------')
        formatted_text_1 = helper.remove_line_feed(random_text_1)
        formatted_text_2 = helper.remove_line_feed(random_text_2)
        new_text = self.__get_new_text(formatted_text_1, formatted_text_2, n1, n2)
        print(new_text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_new_text(text_1: str, text_2: str, n1: int, n2: int) -> str:
        try:
            words_array_1 = re.findall(r"[\w']+", text_1)
            words_array_2 = re.findall(r"[\w']+", text_2)
            new_text = ' '.join([' '.join(words_array_1[:n1]), ' '.join(words_array_2[-n2:])])
            return new_text
        except Exception as e:
            print(f'Ошибка: {e}')
