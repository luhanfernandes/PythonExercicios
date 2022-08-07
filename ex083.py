lista = []

n = str(input('Digite uma expressão: '))
ladoum = (n.count('('))
ladodois = (n.count(')'))

final = ladoum + ladodois

if final %  2 == 0:
    print('A expressão é valida!')
else:
    print('A expressão não existe!')
