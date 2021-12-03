import re
from helper import Helper


class Task11:

    __task_number = 11

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вывести из строки все слова, где количество гласных букв равно согласным. '
              '\nНайти длину самого короткого слова')
        print('----------------------------------------------------------')
        random_text = helper.get_random_text()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__print_words(formatted_text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_words(text: str):
        try:
            vowels = 'аяоёуюэеыи'
            words_array = re.findall(r"[\w']+", text)
            matched_words = dict()
            for word in words_array:
                count_vowel_letters = sum([1 for letter in str(word).lower() if letter in vowels])
                count_consonant_letters = sum([1 for letter in str(word).lower() if letter not in vowels])
                if count_vowel_letters == count_consonant_letters:
                    matched_words[str(word).lower()] = len(word)
            for word in matched_words:
                print(f'{word}: {matched_words[word]}')
            print('----------------------------------------------------------')
            print(f'Длина самого маленького слова - {min(matched_words.values())}')
        except Exception as e:
            print(f'Ошибка: {e}')
