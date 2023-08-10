print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
tot=0
mulher=0
homem=0
while True:
    idade=int(input('idade: '))
    sexo=str(input('sexo: [M/F]')).strip().upper()[0]
    if  idade>=18:
        tot+=1
    if  sexo in 'Mm':
            homem+=1
    else:
        if sexo in 'Ff' and idade <= 20:
            mulher+=1
    print('-'*20)
    continuar=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if  continuar in 'Ss':
        continue
    else:  
        if  continuar in 'Nn':

            print(f'o total de pessoas com mais de 18 anos: {tot}')
            print(f'ao todo tem {homem} homem cadastrados')
            print(f'e temos {mulher} mulheres com menos de 20 anos')
            break