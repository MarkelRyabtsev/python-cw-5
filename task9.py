import re
from helper import Helper


class Task9:

    __task_number = 9

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Составить программу для вычеркивания из слов текста всех букв, стоящих на нечетных '
              '\nместах после буквы "а"')
        print('----------------------------------------------------------')
        random_text = helper.get_random_short_text_eng()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__print_changed_text(formatted_text, 'a')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __print_changed_text(self, text: str, letter: str):
        try:
            words_array = re.findall(r"[\w']+", text)
            for word in words_array:
                if letter in word:
                    changed_word = self.__remove_odd_letters(word, letter)
                    text = text.replace(word, changed_word)
            print(text)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __remove_odd_letters(word: str, letter: str) -> str:
        try:
            new_word = list(word)
            need_remove = False
            for i in range(1, len(word) + 1):
                if need_remove and i % 2 != 0:
                    new_word[i - 1] = ''
                if new_word[i - 1] == letter:
                    need_remove = True
            return ''.join(new_word)
        except Exception as e:
            print(f'Ошибка: {e}')
