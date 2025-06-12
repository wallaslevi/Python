#Calculo de quantos tijolos serão utilizados em uma parede simples, com uma unica fileira de tijolos. será levado em consideração 10% de margem de segurança para perdas, quebras e sobras. Calculo já esta incluso com argamassa de 1cm= 0.01 m


#Entrada de dados da parede
height=float(input("Digite a altura da paredeem metros: "))
width=float(input("Digite a largura/comprimento da parede em metros: "))
wall_area=height*width

#Entrada de dados do tijolo
brick_height=float(input("Digite a altura do tijolo em metros: "))
brick_width=float(input("Digite a largura/comprimento do tijolo em metros: "))

#Considerando argamassa de 1cm (0.01 m)
brick_area=((brick_height+0.01)*(brick_width+0.01))

#Calculando a quantidade de tijolos com e sem a margem de segurança
total_bricks= wall_area / brick_area 
safely=total_bricks*1.1 #10% a mais

#Saída formatada, arredondamento para baixo.
print(f'A área da parede é de {wall_area:.2f}m²')
print(f'A área do tijolo é de {brick_area:.4f}m²')
print(f'tijolos necessarios sem a margem de segurança {int(total_bricks)}')
print(f'tijolos necessarios com a margem de segurança: {int(safely)}')
