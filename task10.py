from helper import Helper


class Task10:
    __task_number = 10

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Посчитать количество английских букв a и b в слове. В случае если a>b, то необходимо '
              '\nудалить все b. Перевести строчные буквы в заглавные')
        print('----------------------------------------------------------')
        random_word = helper.get_random_word_eng()
        print(random_word)
        print('----------------------------------------------------------')
        self.__print_changed_word(random_word)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_changed_word(word: str):
        try:
            a_count = list(word.lower()).count('a')
            b_count = list(word.lower()).count('b')
            if a_count < b_count:
                sign = '<'
            elif a_count > b_count:
                sign = '>'
            else:
                sign = '='
            print(f'Количество букв "a"({a_count}) {sign} "b"({b_count})')
            changed_word = list(word)
            if a_count > b_count and ('b' in word or 'B' in word):
                if 'b' in word:
                    changed_word.remove('b')
                if 'B' in word:
                    changed_word.remove('B')
            print(''.join(changed_word).upper())
        except Exception as e:
            print(f'Ошибка: {e}')
