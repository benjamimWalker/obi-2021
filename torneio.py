n = ''

for c in range(6):
    n += input()

v = n.count('V')

if v == 1 or v == 2:
    print(3)

elif v == 3 or v == 4:
    print(2)

elif v == 5 or v == 6:
    print(1)

else:
    print(-1)