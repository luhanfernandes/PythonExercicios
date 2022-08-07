totalpessoas = 0
temp = []
princ = []
mai = men = 0

while True:

    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if cont == 'S':
        totalpessoas += 1
    if cont == 'N':
        break

print(f'Os dados foram {princ}')
print(f'O total de pessoas foram cadastradas {totalpessoas} pessoas!')
print(f'O maior pessoa foi {mai} kg!')
for p in princ:
    if p[1] = mai:
        print(f'{p[0]}')
print(f'O menor pesso foi {men} kg!')