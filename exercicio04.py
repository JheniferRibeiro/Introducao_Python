numero1 = int(input("Digite um número: "))
operador = input("Digite um operador: ")
numero2 = int(input("Digite outro número: "))

if operador == "+":
    print(numero1+numero2)
elif operador == "-":
    print(numero1-numero2)
elif operador == "*":
    print(numero1*numero2)
elif operador == "/":
    print(numero1/numero2)
else:
    print("Sinal inválido")
