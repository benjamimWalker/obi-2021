naipes = {'C': [], 'E': [], 'U': [], 'P': []}

cadeia = input()

for c in range(len(cadeia)):
    if cadeia[c].isalpha():
        naipes[cadeia[c]].append(int(cadeia[c-2] + cadeia[c-1]))

for key in naipes.items():
    a = False
    key[1].sort()
    if key[1] == list(range(1, 14)):
        print(0)
        continue
    for c in range(1, 14):
        if key[1].count(c) > 1:
            print('erro')
            a = True
            break
    if a:
        continue

    res = []
    for i in key[1]:
        if i not in res:
            res.append(i)
    print(13 - len(res))
    res.clear()

