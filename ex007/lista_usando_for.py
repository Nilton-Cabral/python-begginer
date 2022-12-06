#Este programa têm como objectivo aceder 
#aos itens de uma lista usando a função for

a=(41 * "=")
b=( 2 * "\n" + 41 * "♤" + 2 * "\n")
c=("\n" + 20 * "=" + " " + 20 * "=")
d=(19 * "=" + "☡" + " " + "☡"+ 19 * "=")


#separacao dos códigos para um melhor percepção e visualização

carnes=["porco","vaca","cabrito"]
for carne in carnes:
   print(a + b + a + "Eu gosto de carne de " + carne + ".")
print(a + b + a + "\nEu gosto de carne de preferência carne de vaca que é muito deliciosa!" + c + "\nEu realmente amo comer carne!")
print(a + b + a )

print(2 * "\n" + 13 * "=" + "Quebra de Página" + 12 * "=")
print(2 * "\n" + d + "Este aviso é para informar que depois desta linha começa um novo exercício")

#criar uma lista vazia
#criar uma lista usando a função for e range
#adicionar a lista criada usando for com a lista vazia

valores=[]
print(a + b + a)
for valor in range(0,11):
    valores.append(valor)

print("Eis o valores da lista:")
for valor in valores:
    print("-",valor)
print(a + b + a)
print("O somatório dos valores da lista é:", sum(valores)) 	
print(a + b + a)

#dando um espaço na tela
print("O valor mínimo da lista é:", min(valores))
print(a + b + a)

print("O valor máximo da lista é:", max(valores))
print(a + b + a)


#termino do exercício anterior
#inicío do novo exercício


print(2 * "\n" + 13 * "=" + "Quebra de Página" + 12 * "=")
print(2 * "\n" + d + "Este aviso é para informar que depois desta linha começa um novo exercício")
print(a + b + a)

#criar uma lista de exercícios com
#números ímpares de 1 a 20

print("Esta é uma lista de números ímpares:")
for impar in range(1,20,2):
       print("-",impar)
    

#criando uma lista de cubos
print(a + b + a)
print("Esta será uma lista de cubos X^3:")
for cubos in range(1,11):
    print("-",cubos ** 3)
    
print(a + b + a)
print(13 * "=" + "Fim do Programa" + 13 * "=")
print(a + b + a)


lista_cubos=[cubos ** 3 for cubos in range(1,11)]
print(lista_cubos)