
totmaiorm21=0
totmaiorh21=0
tothomem20=0
totmulher20=0
totidade=0
mediaidade=0
nome_homem_mais_velho=str()
idade_homem_mais_velho=0
idade_homem_mais_novo=0
nome_homem_mais_novo=str()
nome_mulher_mais_velha=str()
idade_mulher_mais_velha=0
nome_mulher_mais_nova=str()
idade_mulher_mais_nova=0
for p in range(1,5):
    nome=str(input(f'informe o nome da {p} pessoa: ')).strip().upper()
    idade=int(input(f'informe a idade da {p} pessoa: '))
    sexo=str(input(f'informe o sexo da {p} pessoa: [M] ou [F]: ')).strip().upper()
    totidade+=idade
    if  p == 1 and sexo =='M':
        nome_homem_mais_velho=nome
        idade_homem_mais_velho=idade
        nome_homem_mais_novo=nome
        idade_homem_mais_novo=idade
    if  sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho=idade
        nome_homem_mais_velho=nome
    if  sexo =='M' and idade < idade_homem_mais_novo:
        idade_homem_mais_novo=idade
        nome_homem_mais_novo=nome
    if  sexo == 'M' and idade <= 20:
        tothomem20+=1
    if  sexo == 'M' and idade > 20:
        totmaiorh21+=1
    else:
        if  p == 1 and sexo =='F':
            nome_mulher_mais_velha=nome
            idade_mulher_mais_velha=idade
            nome_mulher_mais_nova=nome
            idade_mulher_mais_nova=idade
        if  sexo == 'F' and idade > idade_mulher_mais_velha:
            idade_mulher_mais_velha=idade
            nome_mulher_mais_velha=nome
        if  sexo=='F' and idade < idade_mulher_mais_nova:
            idade_mulher_mais_nova=idade
            nome_mulher_mais_nova=nome
        if  sexo=='F' and idade <= 20:
            totmulher20+=1
        if  sexo=='F' and idade > 20:
            totmaiorm21+=1
mediaidade=totidade/4

print(f'media de idade do grupo: {mediaidade}')
print('-=-'*20)
print(f'nome e idade do homem mais velho: {nome_homem_mais_velho},{idade_homem_mais_velho}')
print('-=-'*20)
print(f'nome e idade do homem mais novo: {nome_homem_mais_novo},{idade_homem_mais_novo}')
print('-=-'*20)
print(f'quantidade de homens acima de 20 anos: {totmaiorh21} e abaixo: {tothomem20}')
print('-=-'*20)
print(f'nome e idade da mulher mais velha: {nome_mulher_mais_velha},{idade_mulher_mais_velha}')
print('-=-'*20)
print(f'nome e idade da mulher mais nova: {nome_mulher_mais_nova},{idade_mulher_mais_nova}')
print('-=-'*20)
print(f'quantidade de mulheres acima de 20 anos: {totmaiorm21} e abaixo: {totmulher20}')