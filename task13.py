import re
from helper import Helper


class Task13:

    __task_number = 13

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print('В тексте все повторяющиеся рядом стоящие символы удалить. Подсчитать количества '
              '\nвхождений каждого символа в строку')
        print('----------------------------------------------------------')
        random_text = helper.get_random_short_text_eng()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__print_count_and_remove_double_letters(formatted_text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __print_count_and_remove_double_letters(self, text: str):
        try:
            words_array = re.findall(r"[\w']+", text)
            matched_symbols = dict()
            for word in words_array:
                changed_word = self.__remove_double_letters(word)
                text = text.replace(word, changed_word)
                for symbol in changed_word:
                    if symbol in matched_symbols:
                        matched_symbols[symbol] += 1
                    else:
                        matched_symbols[symbol] = 1
            print(text)
            for symbol in matched_symbols:
                print(f'{symbol}: {matched_symbols[symbol]}')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __remove_double_letters(word: str) -> str:
        try:
            new_word = list(word)
            for i in range(0, len(word) - 1):
                if i != len(word) and new_word[i] == new_word[i + 1]:
                    new_word[i] = ''
                    new_word[i + 1] = ''
            return ''.join(new_word)
        except Exception as e:
            print(f'Ошибка: {e}')
