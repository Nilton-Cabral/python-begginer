##############################################################################
#                                                                            #
#Este é um exercício python                                                  # 
#Este é um trabalho com listas                                               #
#Primeiramente farei uma lista contendo nomes de alguns amigos               #
#                                                                            #
##############################################################################

a=(41 * "=" + 41 * "♤" + 41 * "=")

print(a, "Seja bem vindo ao projecto \n\t'Trabalho com listas' \n\t*sucessos* ")

lista_de_amigos=["Paulo", "Shelcio", "Leusio"]

##############################################################################
#                                                                            #
#A seguir crio uma variavel contedo a mensagem de convite                    #
#                                                                            #
##############################################################################

mensagem=("Este é um convite formal enviado por Nilton endereçado a ")

##############################################################################
#                                                                            #
#depois crio outra variavel chamada fim_da_mensgem que irá complementar a    #
#mensagem apenas para que nao haja continuacao da mensagem depois do nome na #
#função de imprimir                                                          #
#                                                                            #
##############################################################################

fim_da_mensagem=(" para um jantar entre amigos.\nconto com a sua participação")

###############################################################################
#                                                                             #
#A seguir imprimo o convite                                                   #
#                                                                             #
###############################################################################

print(a)

print(mensagem + lista_de_amigos[0] + fim_da_mensagem)

###############################################################################
#                                                                             #
#A impressão a seguir é apenas para embelezar a tela e mensagem               #
#                                                                             #
###############################################################################

print(a)
print(mensagem + lista_de_amigos[1] + fim_da_mensagem)

###############################################################################
#                                                                             #
#A impressão a seguir é apenas para embelezar a tela e mensagem               #
#                                                                             #
###############################################################################

print(a)
print(mensagem + lista_de_amigos[2] + fim_da_mensagem)

###############################################################################
#                                                                             #
#A impressão a seguir é apenas para embelezar a tela e mensagem               #
#                                                                             #
###############################################################################

print(a)

print("Devido a certos motivos pessoais O {} não poderá comparecer ao jantar".format(lista_de_amigos[1]))
print(14 * "*" + 13 * " " + 14 * "*") 

del lista_de_amigos[1]

print("Eis a lista actual de convidados:\n\n*{} \n*{}\n".format(lista_de_amigos[0],lista_de_amigos[1]))

###############################################################################
#                                                                             #
#adcionando outro convidado                                                   #
#                                                                             #
###############################################################################

lista_de_amigos.append("Pedro")
print(a)
print("Com a falta de um dos convidados será adicionado um novo convidado para o jantar")
print(a)
print("Eis a lista de convidados com um membro substituido:\n\n*{} \n*{}".format(lista_de_amigos[0], lista_de_amigos[1]), "\n*" + lista_de_amigos[2], "\n")
print(14 * "*" + 13 * " " + 14 * "*")
print(a)
print(mensagem + lista_de_amigos[0] + fim_da_mensagem)
print(a)
print(mensagem + lista_de_amigos[1] + fim_da_mensagem)
print(a)
print(mensagem + lista_de_amigos[2] + fim_da_mensagem)
print(a)
###############################################################################  
#                                                                             #
#Adcionando mais três convidados                                              #
#com os comandos:                                                             #
    #insert()                                                                 #
    #insert()                                                                 #
    #append()                                                                 #
#                                                                             #
###############################################################################

lista_de_amigos.insert(0,"Francisco")
lista_de_amigos.insert(3, "Armando")
lista_de_amigos.append("João")

###############################################################################
#                                                                             #
#imprimindo                                                                   #
#                                                                             #
###############################################################################

print("Tendo recebido uma mensagem do restaurante avisando que há uma mesa de jantar ainda maior a lista de convidados terá mais 3 membros")
print(a)
#################################
print("Eis a lista de convidados com mais três membros")
print("\n*" + lista_de_amigos[0] + "\n*" + lista_de_amigos[1] + "\n*" + lista_de_amigos[2])
print("\n*" + lista_de_amigos[3] + "\n*" + lista_de_amigos[4] + "\n*" + lista_de_amigos[5])
print(13 * "*"+ 14 * " " + 13 * "*")

print(a)

print(mensagem + lista_de_amigos[0] + fim_da_mensagem)
print(a)
print(mensagem + lista_de_amigos[1] + fim_da_mensagem)
print(a)
print(mensagem + lista_de_amigos[2] + fim_da_mensagem)
print(a)
print(mensagem + lista_de_amigos[3] + fim_da_mensagem)
print(a)
print(mensagem + lista_de_amigos[4] + fim_da_mensagem)
print(a)
print(mensagem + lista_de_amigos[5] + fim_da_mensagem)
print(a)
#Eliminando alguns convidados da lista
print("O dono do restaurante acabou de informar que a mesa não estará disponível a tempo para o jantar e só tem uma mesa com espaço apenas para dois convidados")
print(a)

#Membros eliminados
membro_1=(lista_de_amigos.pop(0))
membro_2=(lista_de_amigos.pop(2))
membro_3=(lista_de_amigos.pop(2))
membro_4=(lista_de_amigos.pop(2))

#informando aos convidados 
print("Lamento informar que a mesa não estará disponível para o jantar! \nPor forma a diminuir a lista de convidados você {} não faz mais parte da lista de convidados".format(membro_1))
print(a)
print("Lamento informar que a mesa não estará disponível para o jantar! \nPor forma a diminuir a lista de convidados você {} não faz mais parte da lista de convidados".format(membro_2))
print(a)
print("Lamento informar que a mesa não estará disponível para o jantar! \nPor forma a diminuir a lista de convidados você {} não faz mais parte da lista de convidados".format(membro_3))
print(a)
print("Lamento informar que a mesa não estará disponível para o jantar! \nPor forma a diminuir a lista de convidados você {} não faz mais parte da lista de convidados".format(membro_4))
print(a)

#Exibindo a lista actual
print("Ainda fazem parte da lista de convidados os seguintes:", "\n*" + lista_de_amigos[0], "\n*" + lista_de_amigos[1])

#Eliminando todos convidados e esvaziando a lista
del lista_de_amigos[0]
del lista_de_amigos[0]
print(a)
#Exibindo a lista de convidados vazias
print("Exibindo a lista de convidados vazia")
print(lista_de_amigos)