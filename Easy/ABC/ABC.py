import sys

lista = sorted(list(map(int,sys.stdin.readline().split(' '))))
letters = list(sys.stdin.readline().strip())
dictionary = {"A": lista[0], "B": lista[1], "C": lista[2]}
listb = []
for i in letters:
    listb.append(dictionary[i])
print(*listb)


"""
letters = letters.replace('A', '0')
letters = letters.replace('B', '1')
letters = letters.replace('C', '2')
letters = letters.strip()
listb = []
for i in letters:
    listb.append(lista[int(i)])
print(*listb)
"""


