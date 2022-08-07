#PROGRAMA QUE LEIA UMA FRASE E MOSTRE:
letra = input('Digite uma frase: ').strip()
letra = letra.upper()

#QUANTAS VEZES APARECE A LETRA ''A''

print(f'A letra A aparece {letra.count("A")} vezes!')

#A POSIÇÃO QUE APAREECE PELA PRIMEIRA VEZ


print(f'A letra A aparece pela primeira vez na posição: {letra.find("A")+1}')

#A ULTIMA POSIÇÃO QUE ELE APARECE
print(f'A ultima letra A aparece pela ultima vez na posição: {letra.rfind("A")+1}')