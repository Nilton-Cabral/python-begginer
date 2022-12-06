#Exercício-trabalhando com listas
#Este exercício python é um trabalho com listas usando métodos de organização de listas
#criando uma lista de países não organizada de forma alfabética
lista=["Moçambique","Angola","Zâmbia","Brasil"]
#imprimindo a lista na sua forma 2
print("Está é a lista na sua forma original:\n",lista)
#imprimindo a lista de forma alfabética
print("Esta é a lista organizada de forma alfabética temporária:\n", sorted(lista))
#imprimindo a lista de forma alfabética reversa
print("Esta é a lista organizada alfabeticamente de forma reversa:\n", sorted(lista,reverse=True))
#imprimindo a lista novamente na sua forma original
print("Eis a lista novamente na sua forma original:\n", lista)
#imprimindo a lista no sentido reverso
lista.reverse()
print("Eis a lista no sentido reverso:\n", lista)
#imprimindo a lista para sua forma original usando o comando #reverse#
lista.reverse()
print("Eis a lista na sua forma original usando o comando reverse:\n", lista)
#imprimindo a lista de forma alfabética permanentemente
lista.sort()
print("Eis a lista organizada de forma alfabética permanentemente:\n", lista)
#imprimindo a lista de forma alfabética reversa permanentemente
lista.sort(reverse=True)
print("Eis a lista organizada de forma alfabética reversa permanentemente:\n", lista)

print(41 * "*")
#usando laço em um lista
for país in lista:
    print(país)
