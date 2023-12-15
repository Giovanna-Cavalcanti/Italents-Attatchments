print("\n******Digite o nome do aluno e sua média e veja se foi aprovado" 
      "ou reprovado!******\n")

aluno = {}

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['média'] = float(input("Digite a média do aluno: "))

if aluno['média'] >= 7:
  print(f"\nO aluno {aluno['nome']} foi aprovado!")
elif aluno['média'] < 7 and aluno['média'] >= 5:
  print(f"\nO aluno {aluno['nome']} está de recuperação!")
else:
  print(f"\nO aluno {aluno['nome']} foi reprovado!")


print("\nFim do programa!\n")
