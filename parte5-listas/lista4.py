lista = [ 5, 12, 8, 20, 3, 15]
numero = int(input("Quantos numeros são maiores que 10: "))
count = 0
for i in lista:
    if i > 10:
        count += 1
print("A quantidade de numeros maiores que 10 é: ", count)