# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

num = int(input('Введите натуральную степень: '))
file_path = 'dz_4_4.txt'
lst = ' = 0'
for i in range(num + 1):
    kf = random.randint(1, 100)
    if kf != 0:
        if  i == 0:
            lst = str(kf) + lst
        else:
            if i == 1:
                lst = str(kf) + '*x' + ' + ' + lst
            else:
                lst = str(kf) + '*x^' + str(i) + ' + ' + lst
            if kf == 1:
                lst = lst[2:]
with open(file_path, 'w') as f:
    f.write(lst)