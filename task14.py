from helper import Helper


class Task14:

    __task_number = 14

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Изменить строку таким образом, чтобы все различные символы остались по одному разу, причем '
              '\nостаются последние вхождения этих символов в строку')
        print('----------------------------------------------------------')
        random_text = helper.get_random_short_text_eng()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__find_last_entry(formatted_text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __find_last_entry(text: str):
        try:
            new_text = list(text)
            last_entries = dict()
            for i in range(0, len(text)):
                if text[i] != ' ':
                    last_entries[text[i]] = i
            for i in range(0, len(text)):
                if i not in last_entries.values() and new_text[i] != ' ':
                    new_text[i] = ''
            print(''.join(new_text))
        except Exception as e:
            print(f'Ошибка: {e}')
