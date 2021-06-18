# Esse código só acerta alguns poucos casos de teste
n = int(input())
amigos = dict()
final = dict()

registro = []

for c in range(n):
    registro.append(input().split())
    registro[c][1] = int(registro[c][1])

for c in range(n):
    if registro[c][0] == 'R':
        if not registro[c][1] in amigos:
            amigos[registro[c][1]] = list()
            amigos[registro[c][1]].append(0)
            amigos[registro[c][1]].append(True)
        else:
            amigos[registro[c][1]][1] = True
        for amigo in amigos:
            if registro[c][1] != amigo and amigos[amigo][1]:
                amigos[amigo][0] += 1
    if registro[c][0] == 'T':
        for amigo in amigos:
            amigos[amigo][0] += int(registro[c][1])

    if registro[c][0] == 'E':
        amigos[registro[c][1]][1] = False
        for amigo in amigos:
            if registro[c][1] != amigo and amigos[amigo][1]:
                amigos[amigo][0] += 1

ordenado = sorted(amigos.items())
for k, v in ordenado:
    print(f'{k} {-1 if v[1] else v[0]}')
