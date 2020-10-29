
#Exercise_1
a = 1256983
b = a % 28
print(b)

#Exercise_2
print(12**52 / 15 < 8 or 3**5 > 100)
print(5 * (3**3) != 900 / 75)

#Exercise_3
print('[[]]'[0:2:] + 'PYTHON' + '[[]]'[2:4:])
print('PYTHON'[4:6:] * 4)
print('PERL'[2] * 6)

#Exercise_4
p = 'python'
print(p[0:len(p) // 2:].upper() + p[len(p) // 2: len(p):])
print(p[0] * len(p))
print('git'[0] * len('git'))

#Exercise_5
#print(7+3*2) - 13
#print('7' + str(3*2)) - 76
#print('7' + '3*2') - 73*2
#print('7' + 3*2) - error protože je každý jiného datového typu

#Exercise_6
hobby = 'music'
print('My hobby is {0}'.format(hobby))
from datetime import date
d = date.fromisoformat('2018-11-01')
print('{:%d/%m}'.format(d))

#Exercise_7
list = []
list.append('music')
list.append('books')
list.append('mathematics')
list.append('baking')
print(list[0])
print(list[3])
del list[0:4:]

#Exercise_8
cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
print(cities)
print('*'.join(cities))

#Exercise_9
alphabet = 'abcdefghijklmnopqrstuvwxyz'
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
a = set(alphabet)
z = set(zen.lower())
print(a.difference(z))

#Exercise_10
d = {'python':'An interpreted, object-oriented programming language'}
dictionary = {('Eliska', 'Radikovska'):'775647383'}

#Exercise_11
info = {('Name', 'Surname'):('John', 'Doe')}
print('_'.join(info[('Name', 'Surname')]))