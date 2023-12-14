print("\n*****Reajuste Salarial*****\n")

salario = float(input("Digite o salário: "))

while salario <= 0:
  print("\nO salário não pode ser negativo :(")
  salario = float(input("\nDigite o salário: \n"))

if salario <= 280:
  percentual = 20
  salario1 = salario + (salario * percentual / 100)
  print("Salário antes do reajuste: R$", salario, "\nPercentual de aumento aplicado: ",
         percentual, "%\nValor com aumento aumento: R$", salario1)
elif salario > 280 and salario <= 700:
  percentual = 15
  salario1 = salario + (salario * percentual / 100)
  print("Salário antes do reajuste: R$", salario, "\nPercentual de aumento aplicado: ",
     percentual, "%\nValor com aumento aumento: R$", salario1)
elif salario > 700 and salario <= 1500:
  percentual = 10
  salario1 = salario + (salario * percentual / 100)
  print("Salário antes do reajuste: R$", salario, "\nPercentual de aumento aplicado: ",
     percentual, "%\nValor com aumento aumento: R$", salario1)
else:
  percentual = 5
  salario1 = salario + (salario * percentual / 100)
  print("Salário antes do reajuste: R$", salario, "\nPercentual de aumento aplicado: ",
     percentual, "%\nValor com aumento aumento: R$", salario1)

  
print("\nfim do programa :)\n")


