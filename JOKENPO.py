# Classico jogo JO KEN PO

from random import randint
from time import sleep

opc=("Pedra","Papel","Tesoura")
computador=randint(0,2)
jogador=int(input("""Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA 
    Qual é sua jogada? """))

print('\033[1;34;47mJO\033[0m')             
sleep(1)
print("\033[1;31;47mKEN\033[0m")
sleep(1)
print('\033[1;30;47mPO\033[0m')
sleep(1)

print("="*35)
print(f'Computador jogou {opc[computador]}') #requisita o valor da tupla na posição que o computador randomicamente escolheu
print(f'Você jogou {opc[jogador]}') #requisita o valor da tupla na posição que o jogador escolheu
print("="*35)

if  computador == 0: # PEDRA
    
    if  jogador == 0:
        print(f"\033[1;31;47mEmpate, ambos escolheram pedra\033[0m")
    elif jogador ==1:
        print(f'\033[1;31;47mVocê ganhou, papel ganha de pedra\033[0m')
    elif jogador ==2:
        print(f'\033[1;31;47mVocê perdeu, pedra ganha de tesoura\033[0m')
    else: print("Jogada inválida")

elif computador == 1: # PAPEL
    
    if  jogador == 0:
        print(f'\033[1;31;47mVocê perdeu, papel ganha de pedra\033[0m')
    elif jogador ==1:
        print(f'\033[1;31;47mEmpate, ambos jogaram papel\033[0m')
    elif jogador ==2:
        print(f'\033[1;31;47mVocê ganhou, tesoura ganha de papel\033[0m')
    else: 
        print("Jogada inválida")

elif computador ==2:  # TESOURA
    
    if  jogador == 0:
        print(f'\033[1;31;47mVocê ganhou, pedra ganha de tesoura\033[0m')
    elif jogador ==1:
        print(f'\033[1;31;47mVocê perdeu, tesoura ganha para papel\033[0m')
    elif jogador ==2:
        print(f'\033[1;31;47mEmpate, ambos jogaram tesoura\033[0m')
    else:
        print("Jogada inválida")
else:
    print("Jogada inválida")