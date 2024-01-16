# Em Python, dicionários são arrays assosiativos, sendo vinculados por uma chave.

# Exemplo

dicionarioSites = {"Jhenifer": "jheniferribeirolopes_@hotmail.com"}
print(dicionarioSites['Jhenifer'])
# A chave se torna 'Jhenifer'. Ao chama-lá, ela irá associar as informações contidas no dicionário e irá retornar as mesmas.


# Caso tenha vários elementos, utilize laços para imprimir

dicionarioSites01 = {"Mae": "Marcia", "Filha": "Jhenifer", "Irmão": "Ricardo"}

for chave in dicionarioSites01:
    print(dicionarioSites01[chave])
    
meuDicionario = {"1":"Jhenifer","2":"Ribeiro","3":"Lopes"}

for keys in meuDicionario:
    print(keys+":"+meuDicionario[keys])
    
for i in meuDicionario.items():
    print(i)