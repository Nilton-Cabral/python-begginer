#criando programa para testes de instruções if
print("Testes com instruções if")
a=(41*"=" + 41*"♤" + 41*"=")
print(a)

#criando uma variável e testando uma instrução if
alien_color="green"
if alien_color == "green":
    print("você ganhou 5 pontos")
if alien_color != "green":
    print("você ganhou 10 pontos")
print(a)
#usando idades

idade=int(input("Digite a sua idade\n:"))

if idade < 2:
   print("você ainda é um bebê")
elif idade < 4:
   print("você é uma criança")
elif idade < 13:
   print("você é um/a menino/a")
elif idade < 18:
   print("você é um/a adolescente")
elif idade < 65:
   print("você já é adulto/a")
else:
    print("você é idoso/a")
print(a)

#if em listas
frutas=["maçã","Laranja","Pêra-maçã"]
print("Eis a lista de frutas Lista de frutas")
for fruta in frutas:
   print(fruta)

escolha=input("Digite a sua fruta preferida da lista:")

if escolha in frutas:
   print("A fruta que você escolheu é {}".format(escolha))
else:
    print("O item desejado não consta na lista")

