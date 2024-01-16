minhaLista = ["pc", "notebook", "celular"]

# para cada item da minha lista, imprima o item
for item in minhaLista:
    print(item)

    # Método 'append' adiciona elementos em uma lista

minhaLista02 = ["Jhenifer", "Ricardo", "Luiz"]

minhaLista02.append("Marcia")
print(minhaLista02[3])

if "Marcia" in minhaLista02:
    print("Marcia esta na lista")

    # Palavra 'del' remove item(s) de uma lista

minhaLista03 = [1, 2, 3, 4, 5]

del minhaLista03[3:]
print(minhaLista03)

#Deleta a lista inteira
del minhaLista03[:]

    # O método 'sort' ordena a lista de modo crescente

lista = [1,25,3,4,854,4185]

lista.sort()
print(lista)

#O paramêtro 'reverse=True' inverte a ordem de crescente ou decrescente

lista.sort(reverse=True)
print(lista)

# 'reverse' inverte a ordem da lista criada

lista01 = [1,5,6]

lista01.reverse()
print(lista01)

######## Os mesmos métodos servem para strings(letras), sendo assim, as ordenando em ordem alfabética.

