#Eliminando espaços nas variáveis
a=(" Jota ")
print("A palavra é", "-" + a + "-", "\n\tSem espaço no lado esquerdo:\n\t" + "-" + a.lstrip() + "-", "\n\tSem espaço no lado direito:\n\t" + "-" + a.rstrip() + "-", "\n\tsem espaços:\n\t" + "-" + a.strip() + "-")
