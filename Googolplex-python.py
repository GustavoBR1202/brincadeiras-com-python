import time

print('''
GOOGOLPLEX PYTHON COUNTER

Insert a number to calculate with googol
''')

val = 0
sec = 0
googol = 1*10**100
x = 1
challenge = int(input())*googol
multiplier = int(input("n\Insert the multplier: "))

print(f"Our challenge: {challenge}, multiplying with {multiplier}")
time.sleep(1)
input("Ready?")

while x <= challenge:
    x = x*multiplier
    #sec = sec+0.1
    #time.sleep(0.1)
    val+=1
    print(f'Valor {val} = {x}')

print('Resultado = ',x)
    

