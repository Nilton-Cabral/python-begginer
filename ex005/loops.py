# criando loops ou laços

# Definindo uma flag
var = 5

# Criando o loop
while var > 0:
    print("Tentativas:", var)
    criador_python = input("Digite o nome do criador da linguagem python: ")
    
    nome = "Guido Van Rossum"
    if criador_python == nome:
        print("voce acertou")
        break
    elif criador_python != (nome and ""):
        print("voce errou! \nTente novamente")
        var -= 1
        continue
    elif criador_python == "":
        pass
    
        

