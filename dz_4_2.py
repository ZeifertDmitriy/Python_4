# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math


num = int(input('Введите натуральное число: '))
spisok =[]
while num % 2 == 0:
    spisok.append(2)
    num = num / 2
for i in range(3, int(math.sqrt(num)) + 1):
    while (num % i == 0):
        spisok.append(i)
        num = num / i
spisok.append(int(num))
print(spisok)