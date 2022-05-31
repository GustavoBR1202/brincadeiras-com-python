import random
from random import choice

participantes = []#coloque aqui as pessoas que vão participar do sorteio, colocando o nome entre aspas simples ('') e separando com virgula (,)
escolhas = 0
vencedor = []

while escolhas <= 9:
    sorteado = random.choice(participantes)
    if sorteado not in vencedor: #verifica se a pessoa foi sorteada duas vezes
        escolhas += 1
        print(f"Vencedor {escolhas} = {sorteado}")
    
