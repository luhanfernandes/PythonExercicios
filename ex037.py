num = int(input('Digite um número inteiro: '))

escolha = int(input('- Digite 1 para \33[31mbinário\33[m \n- Digite 2 para \33[34moctal\33[m \n- Digite 3 para \33[35mhexadecimal\33[m\nSua escolha: '))

if escolha == 1:
    print(bin(num))
elif escolha == 2:
    print(oct(num))
elif escolha == 3:
    print(hex(num))