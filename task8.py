import re
from helper import Helper


class Task8:

    __task_number = 8

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Составить таблицу слов данного текста, начинающихся с буквы "а", '
              '\nс указанием числа повторений каждого слова')
        print('----------------------------------------------------------')
        random_text = helper.get_random_text_eng()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__print_words_started_with_letter(formatted_text, 'a')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_words_started_with_letter(text: str, letter: str):
        try:
            words_array = re.findall(r"[\w']+", text)
            matched_words = dict()
            for word in words_array:
                if word[0] == letter.capitalize() or word[0] == letter.lower():
                    if word in matched_words:
                        matched_words[word] += 1
                    else:
                        matched_words[word] = 1
            for word in matched_words:
                print(f'{word}: {matched_words[word]}')
        except Exception as e:
            print(f'Ошибка: {e}')
