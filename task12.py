import random
import re

from helper import Helper


class Task12:

    __task_number = 12

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вывести из строки слова, которые являются числами, кратными заданному числу m')
        print('----------------------------------------------------------')
        random_text = helper.get_text_with_numbers()
        multiplicity = random.randint(1, 10)
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__print_numbers(formatted_text, multiplicity)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_numbers(text: str, multiplicity: int):
        try:
            print(f'Кратность: {multiplicity}')
            numbers_array = re.findall(r"[\d+']+", text)
            matched_numbers = set()
            for number in numbers_array:
                if str(number).isdigit():
                    if int(number) % multiplicity == 0:
                        matched_numbers.add(int(number))
            if len(matched_numbers) > 0:
                print(f'Числа кратные {multiplicity}: {list(matched_numbers)}')
            else:
                print(f'Чисел кратных {multiplicity} нет.')
            print('----------------------------------------------------------')
        except Exception as e:
            print(f'Ошибка: {e}')
