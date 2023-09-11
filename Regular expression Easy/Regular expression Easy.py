#Задача:
#Найти все адреса почтовых ящиков в тексте.

import re

text = "Почты моих сотрудников artem@mail.ru, proger328@gmail.com и ermilov1@yandex.ru. И мой mail:glava@edu.itmo.ru или на @yandex.ru"
posts = []
for match in re.finditer(r""" (?P<name>[a-zA-Z0-9.]+)      #Имя почтового ящика
                   @(?P<secondlevelDomain>[a-zA-Z.]+)      #Домен второго уровня
                   (\.(?P<toplevelDomain>[a-zA-Z]+))       #Домен верхнего уровня
                   """, 
                   text, re.VERBOSE):
    posts.append(match)
for post in posts:
    print(post.groupdict())