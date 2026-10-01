positivo = 0
num1 = float(input("Digite um número:(0 para sair) "))
while num1 != 0:
    if num1 > 0:
        positivo += 1
    num1 = float(input("Digite um número:(0 para sair) "))
print("A quantidade de números positivos digitados é: ", positivo)
