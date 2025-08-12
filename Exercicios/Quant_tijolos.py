#Calculo de quantos tijolos serão utilizados em uma parede simples, com uma unica fileira de tijolos. será levado em consideração a margem de segurança para perdas, quebras e sobras que preferir. Calculo já esta incluso com argamassa de 1cm²


# Variável que controla se o programa continuará rodando
continuar=True


# Loop principal que mantém o programa funcionando até o usuário decidir sair
while continuar:
    
    
    # Solicita ao usuário a altura da parede (em metros), substituindo vírgula por ponto para evitar erro em todas as variaveis
    altura=float(input("Informe a altura da parede:  ").replace(",", "."))
    comprimento=float(input("Informe o comprimento da parede: ").replace(",", "."))
    altura_tijolo=float(input("Informe a altura do tijolo em metros: ").replace(",", "."))
    comp_tijolo=float(input("Informe o comprimento do tijolo em metros: ").replace(",", "."))
    

    # Verifica se todos os valores informados são maiores que zero (válidos para cálculo)
    if  altura > 0 and comprimento > 0 and altura_tijolo > 0 and comp_tijolo > 0:
        
        # Calcula a área da parede (altura x comprimento)
        area_parede=altura*comprimento
        
        # Calcula a área de cada tijolo considerando a argamassa de 1 cm (0.01 metros)
        # Somamos 0.01 a altura e ao comprimento do tijolo para incluir essa margem
        area_tijolo=(altura_tijolo+0.01)*(comp_tijolo+0.01)
        
        # Calcula quantos tijolos são necessários para cobrir a parede
        total_tijolo=area_parede/area_tijolo
        print("Recomendado entre 10 e 15%")
        
        # Solicita a margem de segurança desejada pelo usuário (em porcentagem)
        escolha=float(input("Qual porcentagem de margem de segurança deseja? ").replace(",", "."))
        
        # Verifica se a margem informada está entre 0 e 100%
        if  0<escolha<100:
            
            # Calcula o total de tijolos com a margem de segurança incluída
            margem=total_tijolo*(1+escolha/100)
            
            # Exibe a quantidade de tijolos sem arredondar (com duas casas decimais)
            print(f'Total de tijolos a serem utilizados SEM a margem de segurança {total_tijolo:.2f} ')
            print(f'Total de tijolos a serem utilizados COM a margem de segurança {margem:.2f}')
            
            # Pergunta ao usuário se deseja sair do programa
            sair=input("Digite S para sair ").upper()
            if  sair=="S":
                continuar=False
        else:
            
            # Caso a margem de segurança seja inválida, pede para tentar novamente ou sair
            sair=input("Valores invalidos, tente novamente ou digite S para sair").upper()
            if  sair=="S":
                continuar=False
    else:

        # Caso algum valor informado seja menor ou igual a zero, pede para tentar novamente ou sair
        sair=input("Valores invalidos, tente novamente ou digite S para sair").upper()
        if  sair=="S":
            continuar=False
