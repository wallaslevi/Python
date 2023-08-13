print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
tot=0
maisd1000=0
maisbarato=0
nomemaisbarato=str()
cont=0
while True:
    produto=str(input('Nome do Produto: '))
    preco=int(input('Preço: '))
    tot+=preco
    cont+=1
    if  cont==1 or preco < maisbarato:
        maisbarato=preco
        nomemaisbarato=produto
    if  preco > 1000:
        maisd1000+=1
    continuar=str(input('quer continuar? [S/N]')).strip().upper()[0]
    if  continuar in 'Ss':
        continue
    else:
        print(f'temos {maisd1000} produtos custando mais de 1000')
        print(f'o total da compra foi {tot}')
        print(f'o produto mais barato foi {nomemaisbarato} que custa {maisbarato}')