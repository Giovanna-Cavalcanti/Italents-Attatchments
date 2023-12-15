import random

print("\n*****Gerador de palpites para Mega sena")

quantidade_de_apostas = int(input("\nQuantas apostas você deseja gerar? "))

palpites = []

print("\nGerando", quantidade_de_apostas, "apostas...")

for _ in range(quantidade_de_apostas):
    aposta = random.sample(range(1, 61), 6)
    palpites.append(aposta)

print("\nAqui estão suas apostas:")
print(palpites)
  
