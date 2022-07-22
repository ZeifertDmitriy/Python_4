# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Первый словарь

file_path_1 = 'dz_4_5_1.txt'
with open(file_path_1, 'r') as f:
    st = f.read()
st = st.split(' ')
st = st[:-2]
slov_1 = {}
for i in range(len(st)):
    if st[i] == '+':
        continue
    elif st[i] == '-':
        st[i + 1] = '-' + st[i + 1]
        continue
    try:
        st[i].index('*')
    except ValueError:
        try:
            st[i].index('x')
        except ValueError:
            mch = st[i]
        else:
            mch = '1'
    else:
        mch = st[i][:st[i].index('*')]
    try:
        st[i].index('x')
    except ValueError:
        step = 0
    else:
        try:
            st[i].index('^')
        except ValueError:
            step = 1
        else:
            step = int(st[i][st[i].index('^')+1:])
    slov_1 [step] = mch
# Второй словарь
file_path_2 = 'dz_4_5_2.txt'
with open(file_path_2, 'r') as f:
    st_2 = f.read()
st_2 = st_2.split(' ')
st_2 = st_2[:-2]
slov_2 = {}
for i in range(len(st_2)):
    if st_2[i] == '+':
        continue
    elif st_2[i] == '-':
        st_2[i + 1] = '-' + st_2[i + 1]
        continue
    try:
        st_2[i].index('*')
    except ValueError:
        try:
            st_2[i].index('x')
        except ValueError:
            mch = st_2[i]
        else:
            mch = '1'
    else:
        mch = st_2[i][:st_2[i].index('*')]
    try:
        st_2[i].index('x')
    except ValueError:
        step = 0
    else:
        try:
            st_2[i].index('^')
        except ValueError:
            step = 1
        else:
            step = int(st_2[i][st_2[i].index('^')+1:])
    slov_2 [step] = mch
if len(slov_1) >= len(slov_2):
    max_slov = len(slov_1)
else:
    max_slov = len(slov_2)
rez = ' = 0'
print(slov_1)
print(slov_2)
for i in range(max_slov):
    if (slov_1.get(i) == None) and (slov_2.get(i) != None):
        mch = int(slov_2.get(i))
    elif (slov_1.get(i) != None) and (slov_2.get(i) == None):
        mch = int(slov_1.get(i))
    elif (slov_1.get(i) != None) and (slov_2.get(i) != None):
        mch = int(int(slov_1.get(i)) + int(slov_2.get(i)))
    elif (slov_1.get(i) == None) and (slov_2.get(i) == None):
        mch = 0
    if i == 0:
        rez = str(mch) + rez
    else:
        if i == 1:
            rez = str(mch) + '*x' + ' + ' + rez
        else:
            rez = str(mch) + '*x^' + str(i) + ' + ' + rez
        if mch == 1:
            rez = rez[2:]
try:
    rez.index('-')
except ValueError:
    print('')
else:
    rez = rez[:rez.index('-') - 2] + rez[rez.index('-')] + ' ' + rez[rez.index('-') + 1:]
file_path_3 = 'dz_4_5_3.txt'
with open(file_path_3, 'w') as f:
    f.write(rez)