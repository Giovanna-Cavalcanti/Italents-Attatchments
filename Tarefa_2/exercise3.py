print("\n*****Cheque os divisores de um número inteiro*****")

num = int(input("\nDigite um número inteiro: "))

i = 1

while i <= num:
  if num % i == 0:
    print(i)
  i = i + 1

