

times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Bragantino', 'Fortaleza', 'Internacional', 'Corinthians',
         'Fluminense', 'América-MG', 'Atlético-GO', 'São Paulo', 'Ceará', 'Santos', 'Cuiabá', 'Athletico-PR', 'Bahia',
         'Sport', 'Juventude', 'Grêmio', 'Chapecoense')

print(f'\nOs cincos primeiros times são: {times[:5]}')
print('-' * 200)

print(f'\nOs quatros últimos times são: {times[16:]}')
print('-' * 200)

print(f'\nTimes em ordem alfabética: {sorted(times)}')
print('-' * 200)

print(f'\nA Chapecoense esta na {times.index("Chapecoense")+1}° posição')

