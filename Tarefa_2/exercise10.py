import random

print("\n******Jogo da adivinhação******\n")

numero_secreto = int(random.randrange(1,11))

numero_usuario = input("Digite um número de 1 a 10: ")

if numero_usuario == numero_secreto:
  print("\nVocê acertou!")
else:
  print("\nVocê errou!", "O número secreto era: ", numero_secreto)
  
print("\nFim do jogo! :)\n")
