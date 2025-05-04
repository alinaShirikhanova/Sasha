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
