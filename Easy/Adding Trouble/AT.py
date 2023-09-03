from sys import stdin, stdout

A, B, C = map(int,stdin.readline().split())
if A + B == C:
    print("correct!")
else:
    print('wrong!')