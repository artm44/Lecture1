#Задача:
#Найти все адреса почтовых ящиков в тексте.

import re

text = "Почты моих сотрудников artem@mail.ru, proger328@gmail.com и ermilov1@yandex.ru. И мой mail:glava@edu.itmo.ru"
posts = []
for match in re.finditer(r""" (?P<name>[a-zA-Z0-9.]+)      
                   @(?P<secondlevelDomain>[a-zA-Z.]+)      
                   (\.(?P<toplevelDomain>[a-zA-Z]+))       
                   """, 
                   text, re.VERBOSE):
    posts.append(match)
for post in posts:
    print(post.groupdict())