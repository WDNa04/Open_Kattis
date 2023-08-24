import sys

def game(big_list):
    new_big_list = []
    for k in big_list:
        list_original = k[:]
        for i in list_original:
            if i == 0:
                list_original.remove(i)
                list_original.append(0)
        list_new = list_original[:]
        for i in range(3):
            if list_original[i] == list_original[i+1] and list_new[i] != 0:
                list_new[i] = list_original[i] * 2
                list_new[i+1] = 0
        for i in list_new:
            if i == 0:
                list_new.remove(i)
                list_new.append(0)
        new_big_list.append(list_new)
    return new_big_list

def transpose(big_list):
    a, k = 0, 0
    new_big_list = []
    i = 0
    while i < 4:
        line = '0 0 0 0'
        small_list = list(map(int,line.split()))
        new_big_list.append(small_list)
        i += 1
    while a <= 3:
        new_big_list[a][k] = big_list[k][a]
        if k == 3:
            a += 1
            k = 0
            continue
        k += 1
    return new_big_list

def reversing(lista):
    for i in range(len(lista)):
        lista[i] = list(reversed(lista[i]))
    return lista

big_list = []
for i in range(4):
    line = sys.stdin.readline()
    small_list = list(map(int,line.split()))
    big_list.append(small_list)

direction = int(sys.stdin.readline())
if direction == 0:
    for i in game(big_list):
        print(*i)
elif direction == 2:
    big_list = reversing(big_list)
    big_list = game(big_list)
    big_list = reversing(big_list)
    for i in big_list:
        print(*i)
elif direction == 1:
    big_list = transpose(big_list)
    big_list = game(big_list)
    for i in transpose(big_list):
        print(*i)
elif direction == 3:
    big_list = transpose(big_list)
    big_list = reversing(big_list)
    big_list = game(big_list)
    big_list = reversing(big_list)
    big_list = transpose(big_list)
    for i in big_list:
        print(*i)
