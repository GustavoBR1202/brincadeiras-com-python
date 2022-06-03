import time

tabuleiro = [['A1','A2','A3'],
             ['B1','B2','B3'],
             ['C1','C2','C3']]

#Vitoria = 0

def jogo_da_velha():
    global Vitoria
    Vitoria = 0
    print("Vamos jogar jogo da velha!")
    j1 = input("Insira o nome do Jogador 1 (X): ")
    j2 = input("Insira o nome do Jogador 2 (O): ")
    rodada = 0

    print('''Regras:
- Você deve escolher uma das posições digitando da maneira correta (ex "A1")
- Cada um faz uma jogada por vez
- Vence aquele que fizer uma linha (horizontal, vertical ou diagonalo) primeiro.

    Nosso tabuleiro:

             [A1,A2,A3]
             [B1,B2,B3]
             [C1,C2,C3]

Bom jogo!''')
    
    #time.sleep(5)
    while Vitoria == 0:
        rodada+=1
        print(f'''
Rodada {rodada}
''')
        for i in tabuleiro:
            print(i)
        entrada_j1 = (input(f'Ok, {j1}, escolha a posição em que deseja jogar! '))

        if entrada_j1 == 'A1':
            tabuleiro[0][0] = 'X'
        elif entrada_j1 == 'A2':
            tabuleiro[0][1] = 'X'
        elif entrada_j1 == 'A3':
            tabuleiro[0][2] = 'X'
            #Primeira linha
        elif entrada_j1 == 'B1':
            tabuleiro[1][0] = 'X'
        elif entrada_j1 == 'B2':
            tabuleiro[1][1] = 'X'
        elif entrada_j1 == 'B3':
            tabuleiro[1][2] = 'X'
            #Segunda linha
        elif entrada_j1 == 'C1':
            tabuleiro[2][0] = 'X'
        elif entrada_j1 == 'C2':
            tabuleiro[2][1] = 'X'
        elif entrada_j1 == 'C3':
            tabuleiro[2][2] = 'X'
            #Terceira linha

        if entrada_j1 == 'break':
            break
        if entrada_j1 == 'fim':
            Vitoria = 1
            
        
        time.sleep(0.5)

        verifica_vitoria()

        if Vitoria == 1:
            break

        for i in tabuleiro:
            print(i)

        entrada_j2 = (input(f'Ok, {j2}, escolha a posição em que deseja jogar! '))

        if entrada_j2 == 'A1':
            tabuleiro[0][0] = 'O'
        elif entrada_j2 == 'A2':
            tabuleiro[0][1] = 'O'
        elif entrada_j2 == 'A3':
            tabuleiro[0][2] = 'O'
            #Primeira linha
        elif entrada_j2 == 'B1':
            tabuleiro[1][0] = 'O'
        elif entrada_j2 == 'B2':
            tabuleiro[1][1] = 'O'
        elif entrada_j2 == 'B3':
            tabuleiro[1][2] = 'O'
            #Segunda linha
        elif entrada_j2 == 'C1':
            tabuleiro[2][0] = 'O'
        elif entrada_j2 == 'C2':
            tabuleiro[2][1] = 'O'
        elif entrada_j2 == 'C3':
            tabuleiro[2][2] = 'O'
            #Terceira linha

        if entrada_j2 == 'break':
            break
        if entrada_j2 == 'fim':
            Vitoria = 1
        
        time.sleep(0.5)

        verifica_vitoria()

        if Vitoria == 1:
            break

def verifica_vitoria():
    global Vitoria
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]:
        Vitoria = 1
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]:
        Vitoria = 1
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]:
        Vitoria = 1
    #Horizontal
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        Vitoria = 1
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        Vitoria = 1
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        Vitoria = 1
    #Vertical
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        Vitoria = 1
    elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2]:
        Vitoria = 1
    #Diagonal 1

    vencedor = 'none'

    if Vitoria == True:
        print(f"Fim de jogo! O {vencedor} é o vencedor!")   

        
