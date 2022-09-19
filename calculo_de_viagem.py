valores = input().split()

tempo = int(valores[0])
velocidade = int(valores[1])

combustivel = tempo*velocidade/12
print('%.3f' % combustivel)
