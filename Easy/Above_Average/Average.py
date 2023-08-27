import sys

count = int(sys.stdin.readline())
for i in range(count):
    sample = sys.stdin.readline().strip()
    lista = list(map(int,sample.split()))
    average = sum(lista[1:])/len(lista[1:])
    count_sample = 0
    for i in lista[1:]:
        if i > average:
            count_sample += 1
    print('%0.3f'%(count_sample / len(lista[1:])*100)+'%')