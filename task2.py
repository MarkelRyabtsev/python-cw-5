import re
from helper import Helper


class Task2:

    __task_number = 2

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текст.'
              '\n а) Подсчитать количество слов в данной строке.'
              '\n б) Подсчитать количество букв "а" в последнем слове данной строки.'
              '\n в) Найти количество слов, начинающихся с буквы "б".'
              '\n г) Найти количество слов, у которых первый и последний символы совпадают между собой')
        print('----------------------------------------------------------')
        random_text = helper.get_random_text()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        print(f'а) Количество слов: {self.__get_words_count(formatted_text)}')
        print(f'б) Количество букв "а" в последнем слове данной строки: '
              f'{self.__get_letter_count_in_last_word(formatted_text)}')
        print(f'в) Количество слов, начинающихся с буквы "б": '
              f'{self.__get_words_count_started_with_letter(formatted_text, "б")}')
        print(f'г) Количество слов, у которых первый и последний символы совпадают между собой: '
              f'{self.__get_words_count_with_same_first_last_letter(formatted_text)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_words_count(text: str) -> int:
        try:
            words_array = re.findall(r"[\w']+", text)
            return len(words_array)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_letter_count_in_last_word(text: str) -> str:
        try:
            words_array = re.findall(r"[\w']+", text)
            last_word = words_array[len(words_array) - 1]
            count = 0
            for letter in last_word:
                if letter.capitalize() == 'А':
                    count += 1
            return f'{count} ({last_word})'
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_words_count_started_with_letter(text: str, letter: str) -> str:
        try:
            words_array = re.findall(r"[\w']+", text)
            count = 0
            match_words_array = []
            for word in words_array:
                if word[0].capitalize() == letter.capitalize():
                    match_words_array.append(word)
                    count += 1
            return f'{count} ({match_words_array})'
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_words_count_with_same_first_last_letter(text: str) -> str:
        try:
            words_array = re.findall(r"[\w']+", text)
            count = 0
            match_words_array = []
            for word in words_array:
                if word[0].capitalize() == word[len(word) - 1].capitalize() and len(word) > 1:
                    match_words_array.append(word)
                    count += 1
            return f'{count} ({match_words_array})'
        except Exception as e:
            print(f'Ошибка: {e}')
