import copy
import random


class Helper:

    @staticmethod
    def get_random_text() -> str:
        array_text = ['Пайтон является мультипарадигмальным языком программирования, поддерживающим императивное, '
                      '\nпроцедурное, структурное, объектно-ориентированное программирование, метапрограммирование '
                      '\nи функциональное программирование. Задачи обобщённого программирования решаются '
                      '\nза счёт динамической типизации. Аспектно-ориентированное программирование частично '
                      '\nподдерживается через декораторы, более полноценная поддержка обеспечивается дополнительными '
                      '\nфреймворками. Такие методики как контрактное и логическое программирование можно реализовать '
                      '\nс помощью библиотек или расширений. Основные архитектурные черты — динамическая '
                      '\nтипизация, автоматическое управление памятью, полная интроспекция, механизм обработки '
                      '\nисключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора, '
                      '\nвысокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, '
                      '\nв свою очередь, могут объединяться в пакеты.',
                      'Пайтон поддерживает динамическую типизацию, то есть тип переменной определяется только во '
                      '\nвремя исполнения. Поэтому вместо «присваивания значения переменной» лучше говорить '
                      '\nо «связывании значения с некоторым именем». К примитивным типам в Пайтон относятся '
                      '\nбулевый, целое число произвольной точности, число с плавающей запятой и комплексное число. '
                      '\nИз контейнерных типов в Пайтон встроены: строка, список, кортеж, словарь и множество. '
                      '\nВсе значения являются объектами, в том числе функции, методы, модули, классы. Добавить '
                      '\nновый тип можно либо написав класс, либо определив новый тип в модуле расширения '
                      '\n(например, написанном на языке Си). Система классов поддерживает наследование (одиночное '
                      '\nи множественное) и метапрограммирование. Возможно наследование от большинства '
                      '\nвстроенных типов и типов расширений',
                      'Одной из интересных синтаксических особенностей языка является выделение блоков кода '
                      '\nс помощью отступов (пробелов или табуляций), поэтому в Пайтон отсутствуют операторные '
                      '\nскобки, как в языке Паскаль, или фигурные скобки, как в Си. Такой «трюк» позволяет '
                      '\nсократить количество строк и символов в программе и приучает к «хорошему» стилю '
                      '\nпрограммирования. С другой стороны, поведение и даже корректность программы может '
                      '\nзависеть от начальных пробелов в тексте. Тем, кто привык программировать на языках '
                      '\nс явным выделением начала и конца блоков, такое поведение поначалу может '
                      '\nпоказаться неинтуитивным и неудобным.',
                      'Состав, синтаксис, ассоциативность и приоритет операций достаточно привычны для языков '
                      '\nпрограммирования и призваны минимизировать употребление скобок. Если сравнивать с '
                      '\nматематикой, то приоритеты операторов зеркалируют соответствующие в математике, '
                      '\nпри этом оператор присвоения значения соответствует типографскому. Хотя приоритеты '
                      '\nопераций позволяют не использовать скобки во многих случаях, на анализ больших '
                      '\nвыражений может тратиться лишнее время, в результате чего в таких случаях выгоднее '
                      '\nявно расставлять скобки.',
                      'Выбор языка обычно зависит от решаемых задач, особенностей языков и наличия библиотек, '
                      '\nтребуемых для решения задачи. Одна и та же задача, написанная на разных языках может '
                      '\nсильно розниться по эффективности исполнения, в том числе различия могут быть и при '
                      '\nисполнении в разных операционных системах или при использовании разных компиляторов. '
                      '\nВ общем случае языки можно поделить на интерпретируемые (скриптовые), компилируемые в '
                      '\nпромежуточное представление и компилируемые, что влияет на производительность и '
                      '\nпотребление памяти. Пайтон принято относить к интерпретируемым. Также отдельные языки '
                      '\nмогут иметь свои сильные стороны, в случае Пайтон выделяется лёгкость в написании программ.']
        return array_text[random.randint(0, len(array_text) - 1)]

    @staticmethod
    def get_random_text_eng() -> str:
        array_text = ['Python is an interpreted high-level general-purpose programming language. '
                      '\nIts design philosophy emphasizes code readability with its use of significant '
                      '\nindentation. Its language constructs as well as its object-oriented approach aim to '
                      '\nhelp programmers write clear, logical code for small and large-scale projects. '
                      '\nPython is dynamically-typed and garbage-collected. It supports multiple programming '
                      '\nparadigms, including structured (particularly, procedural), object-oriented and '
                      '\nfunctional programming. It is often described as a "batteries included" language due to '
                      '\nits comprehensive standard library.',
                      'Python is a multi-paradigm programming language. Object-oriented programming and structured '
                      '\nprogramming are fully supported, and many of its features support functional programming '
                      '\nand aspect-oriented programming (including by metaprogramming and '
                      '\nmetaobjects (magic methods)). Many other paradigms are supported via extensions, including '
                      '\ndesign by contract and logic programming. Python uses dynamic typing and a combination '
                      '\nof reference counting and a cycle-detecting garbage collector for memory management. '
                      '\nIt also features dynamic name resolution (late binding), which binds method and variable '
                      '\nnames during program execution.',
                      'Rather than having all of its functionality built into its core, Python was designed to be '
                      '\nhighly extensible (with modules). This compact modularity has made it particularly '
                      '\npopular as a means of adding programmable interfaces to existing applications. '
                      '\nVan Rossum\'s vision of a small core language with a large standard library and easily '
                      '\nextensible interpreter stemmed from his frustrations with ABC, which espoused the opposite '
                      '\napproach. It is often described as a "batteries included" language due to its '
                      '\ncomprehensive standard library.',
                      'The assignment statement (=) operates by binding a name as a reference to a separate, '
                      '\ndynamically-allocated object. Variables may subsequently be rebound at any time to any '
                      '\nobject. In Python, a variable name is a generic reference holder and does not have a fixed '
                      '\ndata type associated with it. However, at a given time, a variable will refer to some '
                      '\nobject, which will have a type. This is referred to as dynamic typing and is contrasted '
                      '\nwith statically-typed programming languages, where each variable may only contain '
                      '\nvalues of a certain type.',
                      'Python uses duck typing and has typed objects but untyped variable names. Type constraints '
                      '\nare not checked at compile time; rather, operations on an object may fail, signifying '
                      '\nthat the given object is not of a suitable type. Despite being dynamically-typed, '
                      '\nPython is strongly-typed, forbidding operations that are not well-defined (for example, '
                      '\nadding a number to a string) rather than silently attempting to make sense of them.']
        return array_text[random.randint(0, len(array_text) - 1)]

    @staticmethod
    def get_random_short_text_eng() -> str:
        array_text = ['Python is an interpreted high-level general-purpose programming language',
                      'This compact modularity has made it particularly popular as a means of adding programmable '
                      '\ninterfaces to existing applications',
                      'Python uses duck typing and has typed objects but untyped variable names',
                      'Variables may subsequently be rebound at any time to any object',
                      'Its design philosophy emphasizes code readability with its use of significant indentation']
        return array_text[random.randint(0, len(array_text) - 1)]

    @staticmethod
    def get_random_word_eng() -> str:
        array_word = ["colony",
                      "duty",
                      "industrial",
                      "quarter",
                      "brass",
                      "signal",
                      "dried",
                      "themselves",
                      "unusual",
                      "caught",
                      "you",
                      "liquid",
                      "plant",
                      "possible",
                      "bound",
                      "some",
                      "call",
                      "attack",
                      "so",
                      "do",
                      "soldier",
                      "trace",
                      "fully",
                      "neck",
                      "got",
                      "finest",
                      "floating",
                      "pretty",
                      "pair",
                      "teeth",
                      "motor",
                      "central",
                      "paragraph",
                      "vapor",
                      "needed",
                      "soil",
                      "excellent",
                      "diagram",
                      "thy",
                      "greater",
                      "border",
                      "root",
                      "root",
                      "information",
                      "effect",
                      "rod",
                      "life",
                      "brave",
                      "tongue",
                      "thirty",
                      "doll"]
        return array_word[random.randint(0, len(array_word) - 1)]

    @staticmethod
    def get_text_with_numbers() -> str:
        array_text = ['Их никак нельзя найти. Только методом перебора, проверяя каждое число от 2 до 50 '
                      '\nпоследовательно, - простое оно или составное? По счастью, список простых чисел до 50 уже'
                      '\nизвестен, поэтому эту надоедливую работу можно не проделывать - она уже сделана до нас. '
                      '\nПервые из простых чисел - 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,...'
                      '\nПервые 15 из них - меньше 50. Все остальные (кроме перечисленных) числа от 2 до 50 - составные']
        return array_text[random.randint(0, len(array_text) - 1)]

    @staticmethod
    def remove_line_feed(text: str) -> str:
        formatted_text = copy.deepcopy(text)
        formatted_text = formatted_text.replace('\n', '')
        return formatted_text

    @staticmethod
    def swap_letters(a: str, b: str):
        temp = a
        a = b
        b = temp
        return a, b
