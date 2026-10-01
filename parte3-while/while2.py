soma = 0
num1 = float(input("Digite um número(0 para sair): "))
while num1 != 0:
    soma += num1
    num1 = float(input("Digite um número(0 para sair): "))
    print("A soma dos números digitados é: ", soma)