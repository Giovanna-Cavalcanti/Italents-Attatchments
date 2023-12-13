print("\n******Digite dois números e cheque qual é o maior******\n")

num1 = int(input("Digite o primeiro número: "))

num2 = int(input("\nDigite o segundo número: "))

if num1 > num2:
  print("\nO número", num1, "é maior que", num2, "\n")
elif num1 == num2:
  print("\nOs números são iguais\n")
else:
  print("\nO número", num2, "é maior que", num1, "\n")
      
