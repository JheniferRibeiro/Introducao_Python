# -*- coding: utf-8 -*-

# Strings
    #Concatenação

a = "Jhenifer"
b = "Ribeiro"
c = "Lopes"

concatenar = a + " " + b + " " + c
print(concatenar)

    #Contagem dos espaços ocupados

tamanho = len(concatenar)
print(tamanho) 

    #Posição do número a ser exibido

seq = "Jhenifer"

letra = seq[3]
print(letra)

letra = seq[1:5]
print(letra)


    #Atribuindo métodos para strings

a = "Jhenifer"
b = "Ribeiro"

concatenar = a + " " + b

print(concatenar)
concatenar = concatenar.lower()
concatenar = concatenar.upper()
print(concatenar)

    #Removendo caracteres especiais

c = "Jhenifer"
s = "Ribeiro"

concatenar = c + " " + s + "\n"

concatenar = concatenar.strip()
print(concatenar)

    #Transformar strings em uma lista

frase = "Dois pratos de trigo para três tigres tristes"

frase = frase.split()
print(frase)

    #Descobrinfo a posição de uma determinada string

frase = "Dois pratos de trigo para três tigres tristes"

retorne = frase.find("tigres")
print(retorne)
print(frase[retorne:])

    #Substituindo strings

frase = "Dois pratos de trigo para três tigres tristes"

frase = frase.replace("tigres", "gatos")
print(frase)