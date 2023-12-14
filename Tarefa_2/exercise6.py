print("\n*****Digite uma nota de 0 a 10 para avaliação*****\n")

nota = float(input("Digite a nota: "))

while nota < 0 or nota > 10:
  print("\nNota inválida")
  nota = float(input("\nDigite a nota: "))

if nota >= 9:
  print("\nNota A\n")
elif nota >= 8:
  print("\nNota B\n")
elif nota >= 7:
  print("\nNota C\n")
elif nota >= 6:
  print("\nNota D\n")
else:
  print("\nNota F\n")

