#Válidando expressões matematicas com parênteses


resp = 'S'  

while resp == 'S':  
    x = input("Digite a expressão: ").strip()  
    lista = []  # Cria uma lista para usar como pilha no controle dos parênteses

    # Percorre cada caractere da expressão
    for i in x:
        if i == '(':  # Se encontrar um parêntese abrindo, adiciona na pilha
            lista.append('(')
        elif i == ')':  # Se encontrar um parêntese fechando
            if lista:  # Se a pilha não estiver vazia, remove o último parêntese aberto
                lista.pop()
            else:  # Se a pilha estiver vazia, significa que fecham parênteses sem abrir
                lista.append(')')  # Marca erro na pilha e sai do loop
                break

    # Após analisar toda a expressão, verifica se a pilha está vazia
    if not lista:
        print("Expressão válida")  
    else:
        print("Expressão inválida")  
    resp = input("Deseja verificar outra expressão? [S/N]: ").strip().upper()
    if resp not in ['S', 'N']:
        print("Resposta inválida. Encerrando o programa.")
        break
