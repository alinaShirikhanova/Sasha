# Дан список.
# Вывести из списка элементы, которые стоят на четных позициях

# lst = [100, 34, 56, 78, 45, 12, 990]
# lst = list(range(0,1001))
#
# for i in range(0,len(lst),2):
#     print(lst[i])

# lst = [1, 2, 3]
# print(lst[10])


# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         print(lst[i])
# lst = [100, 34, 56, 78, 45, 12, 990]
# maxi=lst[0]
# for i in range(len(lst)):
#     if maxi<lst[i]:
#         maxi=lst[i]
# print(maxi)


# Суммировать все элементы из списка
# lst = [100, 34, 56, 78, 45, 12, 990]
# summ = 0
# for i in range(len(lst)):
#     summ += lst[i]
# print(summ)

# Посчитать кол-во отрицательных чисел в списке
# lst = [100, 34, 56, 78, 45, 12, 990]
# g=0
# for i in range(len(lst)):
#     if lst[i]<0:
#         g+=1
# print(g)

# n = int(input())
# lst = []
#
# for i in range(n):
#     lst.append(int(input()))
lst = [100, 34, 56, 78, 45, 12, 990]
# Вывести все элементы списка в обратном порядке
for i in range(len(lst) - 1, -1, -1):
    print(lst[i])
