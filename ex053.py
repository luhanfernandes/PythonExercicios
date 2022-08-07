#ESTUDAR

frase = str(input('Digite uma frase: ')).strip().upper() #recebe palavra, exclui espaços desnecessarios, coloca tudo em maiusculo
palavras = frase.split() #Separa a frase em lista
junto = ''.join(palavras) #Exclui a lista, juntando a frase toda em uma só palavra
inverso = '' #variavel para inverter

for letra in range(len(junto) - 1, -1, -1): #-1 -1 -1 inveter a frase
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')