# Trabalhando com strings

nome, apelido = "Nilton", "Cabral"

# Concatenado strings
nome_completo = nome + " " + apelido
print(nome_completo)

# fatiamento de strings
# imprimindo as primeiras tres letras
print(nome[:3])
#imprimindo as tres ultimas letras
print(nome[4:])

# lendo a quantidade de caracteres
len(nome_completo)

# verificando se a primeira letra é maiuscula
print(nome.istitle())
print(apelido.istitle())

# convertendo a letra em maiusculas
print(nome.upper())
print(apelido.upper())
