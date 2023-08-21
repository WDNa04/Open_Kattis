import sys
sum = 0
i = 0
lista = []
while True:
    line = sys.stdin.readline().strip()
    if line == '-1':
        print(i,sum)
        break
    else:
        a, b, c = map(str,line.split())
        if c == 'right':
            if b in lista:
                sum += lista.count(b) * 20
            sum += int(a)
            i += 1
        else:
            lista.append(b)
