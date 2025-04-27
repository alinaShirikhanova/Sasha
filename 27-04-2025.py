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
import math
print(int(45.67888))
print(round(1.5))
print(math.factorial(5))
h=3
g=1
while h != 0:
    g*=h
    h-=1
print(g)
f = 1
for i in range(1, h + 1):
    f *= i
print(f)

