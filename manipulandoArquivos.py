# -*- coding: utf-8 -*-

    #Utilizaremos o comando "Open".

# read() = Lê o arquivo inteiro
# readline() = Lê uma linha
# readlines() = Lê arquivo e o armazena em uma lista

arquivo = open("meuArquivoTeste.txt")

linhas = arquivo.readlines()

for linha in linhas:
    print(linha)
    
textoCompleto = arquivo.read()
print(textoCompleto)

    #Criando um arquivo 
        #write serve para escrever no arquivo

#Criando um arquivo 
w = open("arquivoTeste2.txt", "a") # w = modificar texto | a = gravar texto

#Escrevendo dentro do arquivo
w.write("Esse e o meu arquivo\n")

#Fechando o arquivo
w.close()

