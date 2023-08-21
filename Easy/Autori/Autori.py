import sys
import string
upper = list(string.ascii_uppercase)
name = sys.stdin.readline()
lista  = [i for i in name if i in upper]
line = ''
for i in lista:
    line += i
print(line)

