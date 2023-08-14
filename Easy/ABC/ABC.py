import sys

lista = sorted(list(map(int,sys.stdin.readline().split(' '))))
letters = sys.stdin.readline()
letters = letters.replace('A', '0')
letters = letters.replace('B', '1')
letters = letters.replace('C', '2')
letters = letters.strip()
listb = []
for i in letters:
    listb.append(lista[int(i)])
print(*listb)



