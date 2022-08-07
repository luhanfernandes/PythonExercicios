import math

num = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))

print(f'O seno vale: {seno:.3f}')
print(f'O cosseno vale: {cos:.3f}')
print(f'A tangente vale: {tan:.3f}')