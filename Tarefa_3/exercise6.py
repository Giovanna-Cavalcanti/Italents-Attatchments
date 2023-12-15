print("\n*****Crie uma matriz com informações de seus clientes,"
    "5 nomes e 5 idades e veja quais deles são maiores de idade*****")

clientes = []
nomes = []
idades = []

for i in range(5):
    nomes.append(input(f"\nDigite o nome do {i+1}° cliente: "))
    idades.append(int(input("Digite a idade do cliente: ")))  
     
clientes.append(nomes)
clientes.append(idades)
print("\nOs clientes são: ", clientes, "\n")

#agora iremos checar as idades e verificar se são maiores de idade

for i in range(5):
    if idades[i] >= 18:
      print(nomes[i], "é maior de idade")
    else:
        print(nomes[i], "é menor de idade")
