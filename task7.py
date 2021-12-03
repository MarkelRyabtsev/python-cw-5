import re
from collections import OrderedDict
from helper import Helper


class Task7:

    __task_number = 7

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текст. Напечатать все слова, отличные от последнего слова, предварительно преобразовав каждое '
              '\nиз них по следующему правилу:'
              '\n 1) оставить в слове только первые вхождения каждой буквы;'
              '\n 2) если слово нечетной длины, то удалить его среднюю букву')
        print('----------------------------------------------------------')
        random_text = helper.get_random_short_text_eng()
        print(random_text)
        print('----------------------------------------------------------')
        self.__print_changed_text(random_text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __print_changed_text(self, text: str):
        try:
            list_text = list(re.findall(r"[\w']+", text))
            last_word = list_text[len(list_text) - 1]
            text = text.replace(str(last_word).lower(), '')
            text = text.replace(str(last_word).capitalize(), '')
            words_array = list(re.findall(r"[\w']+", text))
            for word in words_array:
                changed_word = self.__filter_letters(word)
                if len(changed_word) % 2 != 0 and len(changed_word) > 1:
                    changed_word = self.__remove_middle_letter(changed_word)
                text = text.replace(word, changed_word)
            print(text)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __remove_middle_letter(word: str) -> str:
        try:
            middle_index = int(len(word) / 2)
            new_word = word[:middle_index] + word[middle_index + 1:]
            return new_word
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __filter_letters(word: str) -> str:
        try:
            return ''.join(OrderedDict.fromkeys(word).keys())
        except Exception as e:
            print(f'Ошибка: {e}')
