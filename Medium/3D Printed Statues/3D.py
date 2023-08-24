import sys

count = int(sys.stdin.readline())

i = 0
while True:
    if count == 1:
        print(1)
        break
    elif count >= 2 ** i + 1 and count <= 2 ** (i+1):
        print(i + 2)
        break
    else:
        i += 1
