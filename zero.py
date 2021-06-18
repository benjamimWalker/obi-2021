lista = list()
for c in range(int(input())):
    n = int(input())
    if n == 0:
        if len(lista) > 0:
            lista.pop()
    else:
        lista.append(n)

print(sum(lista))
