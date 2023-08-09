from random import randint

print('vamos jogar par ou impa? [P/I]')
cont=0
vit=0
der=0
while True:
    jog=int(input('digite um valor: '))
    escolha=str(input('Par ou Impar?[P/I]')).strip().upper()[0]
    comp=randint(0,11)
    cont+=1
    while   escolha not in 'PpIi':
        print('apenas P ou I seram validos...')
        escolha=str(input('Par ou Impar?[P/I]')).strip().upper()[0]
    if  (jog+comp)%2==0 and escolha in 'Pp':
        vit+=1
        print(f'deu Par! vc ganhou, computador escolheu {comp} e voce {jog}')
    elif (jog+comp)%2!=0 and escolha in 'Pp':
        der+=1
        print(f'deu impar! vc perdeu, computador escolheu {comp} e voce {jog}')
    elif (jog+comp)%2==0 and escolha in 'Ii':
        der+=1
        print(f'deu Par! vc perdeu, computador escolheu {comp} e vc {jog}')
    elif (jog+comp)%2!=0 and escolha in 'Ii':
        vit+=1
        print(f'deu Impar! voce ganhou, computador escolheu {comp} e voce {jog}')
    encerrar=str(input('deseja encerrar? [S/N]: ')).strip().upper()
    while encerrar not in 'SsNn':
        encerrar=str(input('deseja encerrar? [S/N]: ')).strip().upper()
    if encerrar in 'Ss':
        print(f'voce jogou {cont} vezes, ganhou {vit} e perdeu {der} vezes')
        break