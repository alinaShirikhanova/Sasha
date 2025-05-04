# Дополнительные математические операции в Python
# print(2 ** 3)
# print(10 % 3)
# print(9 // 4)

# # Условный оператор: отрезки значений
# score = 67
# if 0 <= score < 35:
#     print("2")
# elif 35 <= score < 50:
#     print('3')
# elif 50 <= score < 90:
#     print('4')
# elif 90 <= score < 101:
#     print('5')
# else:
#     print('wrong answer')

# Проверить температуру (норма: 36.0-36.9)
# t=float(input())
# if 36.0<=t<37:
#     print('Здоровый')
# else:
#     print('больной')

# age = int(input())
# gender = input()
#
# if age > 18:
#     if gender == 'ж':
#         print('женщина')
#     else:
#         print('мужчина')
# else:
#     if gender == 'ж':
#         print('девочка')
#     else:
#         print('мальчик')
#
# if gender=='ж' and age>=18:
#     print('женщина')
# if gender=='ж' and age<18:
#     print('девочка')
# if gender=='м' and age>=18:
#     print('мужчина')
# if gender=='м' and age<18:
#     print('мальчик')

# x=int(input())
# y=int(input())
# if x>0:
#     if y>0:
#         print('1')
#     else:
#         print('4')
# else:
#     if y>0:
#         print('2')
#     else:
#         print('3')
#
# if x > 0 and y > 0:
#     print('1')
# elif x > 0 and y < 0:
#     print('4')
# elif x < 0 and y < 0:
#     print('3')
# else:
#     print('2')


# x = 5
# if x > 0:
#     if x % 2 == 0:
#         print('положительное четное')
#     else:
#         print('положительное нечетное')

#
# color = input()
# if color == 'красный':
#     print('стоп')
# elif color == 'желтый':
#     print('жди')
# elif color == 'зеленый':
#     print('иди')
# else:
#     print('некорректный цвет')
# import math
# print(int(45.67888))
# print(round(1.5))
# print(math.factorial(5))
# h=3
# g=1
# while h != 0:
#     g*=h
#     h-=1
# print(g)
# f = 1
# for i in range(1, h + 1):
#     f *= i
# print(f)
import math
# print(round(2.6))
# print(round(2.65678, 3))

# print(int(1.9999))
# truncate - отрезать
# ceiling - потолок
# print(math.floor(5.9999))
# print(math.ceil(5.1))
# print(math.trunc(4.9))


# Преобразование типов переменных
# print(int('10'))
# print(int(True))
# print(int(False))
# print(str(False))
# print(int('10'))
# x = 11
# print(x > 10)
# if x > 10:
#     print('x > 10')

# Способы вычисления факториала в Python

a=5
g=1
for i in range(1,a+1):
    g*=i

from math import*
print(factorial(a))


# 16. Понятие цикла и итерации. Операторы break и continue
# Перебрать числа от 1 до 20 и остановиться, если наткнешься на 7
# a=1
# while a<20:
#     print(a)
#     a+=1
#     if a==7:
#         break

# Распечатать все числа от 1 до 30, но пропускать числа, которые делятся на 3
# for i in range(1,31):
#     if i%3==0:
#         continue
#     print(i)

# for i in 'Hello':
#     print(i)
#
# line = 'Hello'
# for i in range(len(line)):
#     print(line[i])

# a=input()
# for i in a:
#     print(i)

# Форматирование строк: f-строки
# name = input()
# age = int(input())
# country = input()

# Привет! Меня зовут <имя>, мне <age> лет. Я из <country>!
# print('Привет! Меня зовут',name,'мне',age,'лет. Я из',country, '!')
# print(f'Привет! Меня зовут {name} мне {age} лет. Я из {country}!')
# print('Мне ' + age + 'лет')





# a = int(input())
# b = int(input())
#
# # 1 + 5 = 6
# print(f'{a} + {b} = {a + b}')

# Операции со строками и функция len()
line = 'Today is a good day'
# print(line + line) # Конкатенация строк
# print('a' * 3)
# print(len(line))
# a = 45
# print(line + a)

# Индексация и итерирование строк

for letter in 'Today is a good day':
    print(letter)

for i in range(0, len(line), 2):
    print(line[i])


