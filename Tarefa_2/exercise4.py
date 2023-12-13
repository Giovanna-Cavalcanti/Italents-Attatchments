print("\n*****Digite um número e verifique se é positivo*****")

num = float(input("\nDigite um número: "))

if num < 0:
  print("\nO número digitado é negativo :(\n")
elif num > 0:
  print("\nO número é positivo :)\n")
else:
  print("\nO número é inválido\n")
