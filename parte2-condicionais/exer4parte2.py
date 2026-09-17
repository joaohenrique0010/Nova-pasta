media = float(input("digite a media do aluno:"))
if media >= 6:
    print(f"o aluno foi aprovado com media {media}")
elif media < 5.9 and media > 4:
    print(f"o aluno ficou de recuperação com media {media}")
else:
    print(f"o aluno foi reprovado com media {media}")
