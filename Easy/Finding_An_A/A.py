import sys

name = sys.stdin.readline().strip()

for i in range(len(name)):
    if name[i] == 'a':
        print(name[i:])
        break