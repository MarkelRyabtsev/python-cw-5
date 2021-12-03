import re
from helper import Helper


class Task6:

    __task_number = 6

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Отредактировать заданное предложения текста, удаляя из него все слова с нечетными номерами и '
              '\nпереворачивая слова с четными номерами. Например, HOW DO YOU DO -> OD OD')
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
            indexes_for_remove = []
            for i in range(0, len(list_text)):
                if (i + 1) % 2 == 0:
                    list_text[i] = self.__reverse_word(list_text[i])
                else:
                    indexes_for_remove.append(i - 1)
            changed_text = " ".join([word for index, word in enumerate(list_text) if index in indexes_for_remove])
            print(changed_text)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __reverse_word(word: str) -> str:
        try:
            return word[::-1]
        except Exception as e:
            print(f'Ошибка: {e}')
