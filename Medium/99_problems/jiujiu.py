import sys

N, Q = map(int, sys.stdin.readline().split())
lista = list(map(int, sys.stdin.readline().split()))
for i in range(Q):
    T, D = map(int, sys.stdin.readline().split())
    if T == 1:
        dicta = {}
        for k in lista:
            if k - D > 0:
                dicta[k] = k - D
        if len(dicta) != 0:
            value = list(dicta.keys())[list(dicta.values()).index(min(dicta.values()))]
            print(value)
            lista.remove(value)
        else:
            print(-1)
    else:
        dictb = {}
        for k in lista:
            if D - k >= 0:
                dictb[k] = D - k
        if len(dictb) != 0:
            value = list(dictb.keys())[list(dictb.values()).index(min(dictb.values()))]
            print(value)
            lista.remove(value)
        else:
            print(-1)
