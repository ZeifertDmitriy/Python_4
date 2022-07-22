# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def povtor(lst, n):
    count = 0
    for i in range(len(lst)):
        if n == lst[i]:
            count += 1
    return count

file_path = 'dz_4_3.txt'
spisok = []
spisok_v = []
with open(file_path, 'r') as f:
    spisok = f.read()
spisok = spisok.split(' ')
for i in range(len(spisok)):
    if povtor(spisok, spisok[i]) < 2:
        spisok_v.append(spisok[i])
print(spisok_v)
