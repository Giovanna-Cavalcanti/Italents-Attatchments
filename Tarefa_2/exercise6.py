print("\n*****Digite uma nota de 0 a 10 para avaliação*****\n")

nota = float(input("Digite a nota: "))

while nota > 0 or nota <= 10:
  if nota >= 9:
    print("\nNota A\n")
    break
  elif nota >= 8:
    print("\nNota B\n")
    break
  elif nota >= 7:
    print("\nNota C\n")
    break
  elif nota >= 6:
    print("\nNota D\n")
    break
  else:
    print("\nNota F\n")
    break
