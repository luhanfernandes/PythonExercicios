peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'Seu imc é {imc:.2f} e você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é {imc:.2f} e você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é {imc:.2f} e você está com sobrepreso!')
elif imc >= 30 and imc < 40:
    print(f'Seu imc é {imc:.2f} e você está com obesidade!')
else:
    print(f'Seu imc é {imc:.2f} e você está com obesidade morbida!')
