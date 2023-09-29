from sys import stdin, stdout

i = 0
listb = []
def movement(n, a,lista, m):
    global i
    global listb
    start = lista[a]
    if i == 0 and start == m:
        return 'magic\n'+str(i)
    elif a+start < 0:
        i += 1
        return 'left\n'+str(i)
    elif a+start > n:
        i += 1
        return 'right\n'+str(i)
    else:
        end = lista[a+start]
        i+=1
        listb.append(a)
        if end == m:
            return 'magic\n'+str(i)
        elif a+start in listb:
            return 'cycle\n'+str(i)
        else:
            return movement(n,a+start,lista,m)


n, s, m = map(int,stdin.readline().split())

lista = list(map(int,stdin.readline().split()))

print(movement(n, s-1, lista, m))