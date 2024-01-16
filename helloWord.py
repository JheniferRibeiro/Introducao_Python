# -*- coding: utf-8 -*-
print("Olá mundo!")

# Operações matemáticas

print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)

# Para elevar números

print(2 ** 2)

# Operador módulo - Retorna o resto da divisão

print(10 % 3)

# Variaveis e tipos de dados

variavel01 = "Mundo" #String
variavel02 = 2       #Integer
variavel03 = 2.2     #Float
variavel04 = True    #Boolean

print(variavel01)
print(variavel02)
print(variavel03)
print(variavel04)

# Operadores lógicos

var1 = 2
var2 = 3
soma = var1 + var2

print(var1 == var2)
print(var1 != var2)
print(var1 > var2)
print(var1 < var2)
print(var1 >= var2)
print(soma == var1 + var2)

# Operadores Lógicos

x = 2
y = 2
z = 3

soma = x + y 

print(x == y and x == soma)
print(x == y or x == soma)
print(x == y or x == soma and x == z)

# Comandos condicionais

variavelX = 5
variavelY = 6

# Comando if:

if variavelY > variavelX:
    print("A variavel Y é maior que a variavel X")
if variavelX > variavelY:
    print("A variavel Y é menor que a variavel X")

# Comando else:
    
if variavelX > variavelY:
    print("A variavel X é maior que a variavel Y")
else:
    print("A variavel X é menor que a variavel Y")

# Comando elif 

a = 5
b = 9

if a == b:
    print("A é igual B")
elif a > b:
    print("A é maior que B")
else:
    print("A é menor que B")



