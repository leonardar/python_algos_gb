"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import heapq

lst = [i for i in range(11)]
lst2 = [i for i in range(13)]
lst3 = [i for i in range(21)]


# Нахождение в массиве медианы
# Делю напополам и заменяю в первой части массива меньший элемент большим из второй части массива
# В первой части массива остаются бОльшие элементы, наименьший элемент из них встаёт на нулевой индекс


def median(l):
    nl = []
    heapq.heapify(nl)
    for i in range(len(l) // 2 + 1):
        heapq.heappush(nl, l[i])
    for i in range(len(l) // 2 + 1, len(l)):
        if l[i] > nl[0]:
            heapq.heapreplace(nl, l[i])
    return nl[0]


print(median(lst))
print(median(lst2))
print(median(lst3))
