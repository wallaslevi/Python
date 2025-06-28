# O bom e velho IMC (Índice de Massa Corporal)
# Utilize a referencia metros para altura Ex: 1.75 

peso=float(input("Qual é seu peso? (Kg) "))
altura=float(input("Qual é sua altura? (M) "))
imc= peso / (altura ** 2)

print(f'{imc:.1f}')

if  imc < 18.5:
    print("Você está abaixo do peso ")
elif imc >=18.5 and imc <= 24.9:
    print("Peso normal ")
elif imc >= 25 and imc <= 29.9:
    print("Você está com sobrepeso ")
elif imc >=30 and imc <= 34.9:
    print("Você está com obesidade grau I ")
elif imc >= 35 and imc <= 39.9:
    print("Você está com obesidade grau II ")
else: 
    imc >= 40
    print("Você está com obesidade grau III")
