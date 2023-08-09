from random import randint
from time import sleep
print('-=-'*20)
opcao=int(input("""informe sua opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA: """))
lista=['PEDRA','PAPEL','TESOURA']
print('-=-'*20)

print('PROCESSANDO...')
computador=randint(0,2)
sleep(2)
if  opcao == computador:
    print(f'EMPATE, o computador jogou {lista[computador]} e voce {lista[opcao]}')
elif opcao==0 and computador==1:
    print(f'VOCE PERDEU, o computador jogou {lista[computador]} e voce {lista[opcao]}')
elif opcao==1 and computador==0:
    print(f'VOCE GANHOU, o computador jogou {lista[computador]} e voce {lista[opcao]}')
elif opcao==0 and computador==2:
    print(f'VOCE GANHOU, o computador jogou {lista[computador]} e voce {lista[opcao]}')
elif opcao==2 and computador==0:
    print(f'VOCE PERDEU, o computador jogou {lista[computador]} e voce {lista[opcao]}')
elif opcao==1 and computador==2:
    print(f'VOCE PERDEU, o computador jogou {lista[computador]} e voce {lista[opcao]}')
elif opcao==2 and computador==1:
    print(f'VOCE GANHOU, o computador jogou {lista[computador]} e voce {lista[opcao]}')
