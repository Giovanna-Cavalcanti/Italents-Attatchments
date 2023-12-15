print("\n******Jogo do Detetive******\n")

print("Responda as perguntas com sim ou não\n")

print("\n1 - Você telefonou para a vítima?")

resposta1 = input()

print("\n2 - Você esteve no local do crime?")

resposta2 = input()

print("\n3 - Você mora perto da vítima?")

resposta3 = input()

print("\n4 - Você devia para a vítima?")

resposta4 = input()

print("\n5 - Você já trabalhou com a vítima?")

resposta5 = input()

respostas = [resposta1, resposta2, resposta3, resposta4, resposta5]

respostas_em_caixa_baixa = [resposta.lower() for resposta in respostas]

respostas_positivas = respostas_em_caixa_baixa.count('sim')

if respostas_positivas == 2:
  print("\nVocê é suspeito!")
elif respostas_positivas == 3 or respostas_positivas == 4:
  print("\nVocê é cúmplice!")
elif respostas_positivas == 5:
  print("\nVocê é o assassino!")
else:
  print("\nVocê é inocente!")

print('\n******Fim do programa******\n')
