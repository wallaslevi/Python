print('='*20)
print('     BANCO     ')
print('='*20)
n50 = n20 = n10 = n1 = 0
saque=int(input('informe o valor do saque: '))
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        elif saque >= 10:
            saque -= 10
            n10 += 1
        elif saque >= 1:
            saque -= 1
            n1 += 1
    if saque == 0:
        break
print(f'Você receberá {n50} notas de 50, {n20} de 20, {n10} de 10 e {n1} de 1.')