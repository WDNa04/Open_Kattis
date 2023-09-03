from sys import stdin, stdout

i = 0
listb = []
def movement(n, a,lista, m):
    global i
    global listb
    start = lista[a]
    if i == 0 and start == m:
        stdout.write('magic\n')
        stdout.write(str(i) + '\n')
    elif a+start < 0:
        i += 1
        stdout.write('left\n')
        stdout.write(str(i) + '\n')
    elif a+start > n:
        i += 1
        stdout.write('right\n')
        stdout.write(str(i) + '\n')
    else:
        end = lista[a+start]
        i += 1
        listb.append(a)
        if end == m:
            stdout.write('magic\n')
            stdout.write(str(i) + '\n')
        elif a+start in listb:
            stdout.write('cycle\n')
            stdout.write(str(i) + '\n')
        else:
            movement(n,a+start,lista,m)


n, s, m = map(int,stdin.readline().split())

lista = list(map(int,stdin.readline().split()))

movement(n, s-1, lista, m)