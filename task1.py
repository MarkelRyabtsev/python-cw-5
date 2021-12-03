import re
from helper import Helper


class Task1:
    __task_number = 1

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текст. Требуется напечатать все слова с удвоенной буквой "н". '
              '\nВывести самое длинное и короткое слово из строки')
        print('----------------------------------------------------------')
        random_text = helper.get_random_text()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__print_words_with_double_letter(formatted_text, 'н')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_words_with_double_letter(text: str, letter: str):
        try:
            words_array = re.findall(r"[\w']+", text)
            double_letters_array = []
            has_double_letter = False
            for word in words_array:
                if f'{letter}{letter}' in word:
                    has_double_letter = True
                    double_letters_array.append(word)
                    print(word)
            if not has_double_letter:
                print(f'Слов с удвоенной \'{letter}\' не найдено')
            else:
                double_letters_array = sorted(list(set(double_letters_array)), key=len)
                max_length = list(filter(lambda x: (len(x) == len(double_letters_array[len(double_letters_array) - 1])),
                                         double_letters_array))
                min_length = list(filter(lambda x: (len(x) == len(double_letters_array[0])), double_letters_array))
                print(f'Самое длинное слово: {max_length}')
                print(f'Самое короткое слово: {min_length}')
        except Exception as e:
            print(f'Ошибка: {e}')
