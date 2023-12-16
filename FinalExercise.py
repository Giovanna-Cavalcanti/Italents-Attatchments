import random

print("\n*****Vamos jogar um jogo de dados!*****")

i = (int(input("\nQuantos jogadores vão jogar? ")))

while i <= 0 or i > 10:
  print("\nNúmero de jogadores inválido!")
  i = (int(input("\nQuantos jogadores vão jogar? ")))

j = (int(input("\nQuantas rodadas? ")))

while j <= 0 or j > 6:
  print("\nNúmero de rodadas inválido!")
  i = (int(input("\nQuantas rodadas vão jogar? ")))

print("\nVamos começar!")

jogadores = []

for _ in range(0, i):
  print(f"\nQual o nome do jogador {_}?")
  jogador = {}
  jogador["nome"] = input()
  jogador["pontos"] = [0]
  jogadores.append(jogador)

for _ in range(0, j):
  for jogador in jogadores:
    print(f"\n{jogador['nome']}, é a sua vez!")
    input("Pressione enter para rolar os dados.")
    dado1 = random.randint(1, 6)
    print(f"\n{jogador['nome']} rolou {dado1}.")
    jogador["pontos"].append(dado1)

#agora vamos checar quem na rodada ganhou, e ordenar os jogadores
#pelo número de vitórias

for jogador in jogadores:
  #vamos somar os pontos de cada jogador
  print("\n----------------------------------------------")
  jogador["pontos"] = sum(jogador["pontos"])
  print(f"\n{jogador['nome']} fez {jogador['pontos']}"
        f" pontos na rodada.")

#ordenalos do maior pro menor
jogadores.sort(key=lambda jogador: jogador["pontos"], reverse=True)
#agora vamos checar quem ganhou, ou se houve empate

print("\n------------------------------------------------")

for i in range(0, len(jogadores)-1):
   if jogadores[i]['pontos'] == jogadores[i+1]['pontos']:
    print(f"\n----Houve empate! entre {jogadores[i]['nome']} e {jogadores[i+1]['nome']}")
else:
  print(f"\n----O vencedor foi {jogadores[0]['nome']}!\n")

  
