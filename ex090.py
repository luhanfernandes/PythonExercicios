aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['Média'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'Nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["Média"]}')

if aluno["Média"] >= 6:
    print('Situação é igual a aprovada!')
else:
    print('Situação é igual a reprovada!')