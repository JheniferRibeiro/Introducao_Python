nota01 = int(input("Digite sua primeira nota: "))
nota02 = int(input("Digite sua segunda nota: "))
resultado = (nota01 + nota02)/2
print(resultado)

if resultado < 6:
    print("Aluno reprovado")
else:
    print("Aluno aprovado")