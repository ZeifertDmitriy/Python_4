# file_path = r'file.txt'
# f = open(file_path, 'r')
# for line in f:
#     print(line, end = '')
# f.close()

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел

# file_path = 'file.txt'
# stroka = []
# with open(file_path, 'r') as f:
#     stroka = f.read()
# stroka = stroka.split(' ')
# for s in range(len(stroka)):
#     stroka[s] = int(stroka[s])
# print(max(stroka))
# print(min(stroka))


# Найдите корни квадратного уравнения Ax2 +Bx + C = 0 двумя способами:
# 1. с помощю математических формул нахождения корней квадратного уравнения
# 2. с помощю дополнительных библиотек Python

# path = 'file2.txt'
# with open(path, 'r') as my_file:
#     data = my_file.read()
# data = data.split()
# data = data[:-2]
# data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
# print(data)
# d = data[1]**2 - 4 * data[0] * data[2]
# print(d)
# x_1 = (-data[1] + d**0.5) / (2 * data[0])
# x_2 = (-data[1] - d**0.5) / (2 * data[0])
# print(x_1, x_2)

# disc

# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.