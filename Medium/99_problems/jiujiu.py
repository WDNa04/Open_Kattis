from sys import stdin, stdout

N, Q = map(int, stdin.readline().split())
lista = list(map(int, stdin.readline().split()))
for i in range(Q):
    T, D = map(int, stdin.readline().split())
    if T == 1:
        dicta = {}
        for k in lista:
            if k - D > 0:
                dicta[k] = k - D
        if len(dicta) != 0:
            value = list(dicta.keys())[list(dicta.values()).index(min(dicta.values()))]
            stdout.write(str(value) + '\n')
            lista.remove(value)
        else:
            stdout.write(str(-1)+'\n')
    else:
        dictb = {}
        for k in lista:
            if D - k >= 0:
                dictb[k] = D - k
        if len(dictb) != 0:
            value = list(dictb.keys())[list(dictb.values()).index(min(dictb.values()))]
            stdout.write(str(value) + '\n')
            lista.remove(value)
        else:
            stdout.write(str(-1)+'\n')
