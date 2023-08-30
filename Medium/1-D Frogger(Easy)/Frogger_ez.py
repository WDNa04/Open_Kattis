import sys

i = 0
listb = []
def movement(n, a,lista, m):
    global i
    global listb
    start = lista[a]
    if start == 0:
        print(i)
    elif i == 0 and start == m:
        print(i)
    elif a+start < 0:
        i += 1
        print('left')
        print(i)
    elif a+start > n:
        i += 1
        print('right')
        print(i)
    else:
        end = lista[a+start]
        i += 1
        listb.append(a)
        if end == m:
            print('magic')
            print(i)
        elif a+start in listb:
            print('cycle')
            print(i)
        else:
            movement(n,a+start,lista,m)


n, s, m = map(int,input().split())

lista = list(map(int,input().split()))

movement(n, s-1, lista, m)