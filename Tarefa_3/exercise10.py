print("\n******Criador de Pessoas******\n")

print("Quantos objetos você deseja criar? ")

n = int(input())
pessoas = []

for i in range(n):
  pessoa = {}
  print(f"\nDigite o nome da {i+1}ª pessoa:")
  pessoa["nome"] = input()
  print("\nDigite o sexo biologico da pessoa, f para feminino e m para masculino:")
  pessoa["sexo"] = input().lower()
  print("---O sexo biológico é válido?---")
  print("1 - Sim")
  print("2 - Não")
  sexo_valido = int(input())
  if sexo_valido == 1:
    pessoa["sexo_valido"] = True
  else:
    pessoa["sexo_valido"] = False
  print("\nDigite a idade da pessoa:")
  pessoa["idade"] = int(input())
  pessoas.append(pessoa)

# O programa deve
# exibir:
# • O total de pessoas cadastradas.
# • A média de idade das pessoas.
# • Uma lista com as mulheres cadastradas.
# • Uma lista com a idade de todas as pessoas que estejam acima da
# média de idade.

print("\n-----------RESULTADOS-----------")

print(f"\nO total de pessoas cadastradas é: {len(pessoas)}")
soma_idade = 0

for i in range(len(pessoas)):
  soma_idade += pessoas[i]["idade"]


media_idade = soma_idade / len(pessoas)

print(f"\nA média de idade das pessoas é: {media_idade}")

print("\nMulheres cadastradas:")
for i in range(len(pessoas)):
  if pessoas[i]["sexo"] == "f":
    print(f"{pessoas[i]['nome']}")

print("\nIdade acima da média de idade:")
for i in range(len(pessoas)):
  if pessoas[i]["idade"] > media_idade:
    print(f"{pessoas[i]['idade']}")


print("\n-----------FIM-----------") 
