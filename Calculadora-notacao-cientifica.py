import time

print('''
CALCULADORA DE NOTAÇÃO CIENTIFICA PYTHON

Insira qual o modo que deseja (1 = Inteiro em notação/2 = Notação em inteiro)''')
tipo = int(input())
time.sleep(1)

if tipo == 1:
    inteiro = int(input('Insira o valor inteiro (será convertido para notação)'))
    print('n\Calculando...')
    #calculo
    digits = len(str(inteiro))
    digits-=1
    
    time.sleep(1)
    print(f"O resultado é: 1 x 10^{digits}")

if tipo == 2:
    mult = int(input('Insira o multiplicado: '))
    exp = int(input('Insira o expoente: '))
    print('n\Calculando...')
    #calculo
    digits = mult*10**(exp)
    
    time.sleep(1)
    print(f"O resultado é: {digits}")
    
