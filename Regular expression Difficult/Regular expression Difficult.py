#Задача:
#Проверка на праивльность скбок {[(
#Пример:
#{([][])} - правильная
#[{(}] - неправильная

import regex

text = input("Введите последовательность скобок:\n")
#text = input()
print(regex.search( r"""^(       
                    (\((?1)*\))| # открывающая скобка - рекурсия - закрывающая скобка
                    (\[(?1)*\])| # ищется одна из трех скобок
                    ({(?1)*})|   # рекурсия для проверки подстроки: {"Подстрока со скобками"}
                    )
                    (?1)*$       # для соседних, ещё не открытых скобок
""",  text, regex.VERBOSE) is not None)