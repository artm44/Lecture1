#Задача:
#Найти все адреса почтовых ящиков в тексте.

import re

text = input("Введите текст:\n")
posts = []
for match in re.finditer(r""" (?P<name>[a-zA-Z0-9.]+)      #Имя почтового ящика
                   @(?P<secondlevelDomain>[a-zA-Z.]+)      #Домен второго уровня
                   (\.(?P<toplevelDomain>[a-zA-Z]+))       #Домен верхнего уровня
                   """, 
                   text, re.VERBOSE):
    posts.append(match)
for post in posts:
    print(post.groupdict())