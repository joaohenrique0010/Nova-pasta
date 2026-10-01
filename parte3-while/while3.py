senha = "senai123"
while True:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta. Tente novamente.")