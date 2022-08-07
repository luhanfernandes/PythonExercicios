n = 0
cont = 0

for c in range(0,501,3):
    if c % 2 == 1:
        cont = cont + 1
        n += c
print(n)
print(cont)