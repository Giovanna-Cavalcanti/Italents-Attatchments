print("\n*****este programa irá ordenar uma lista de números em duas outras listas,"
      " sendo elas dos pares e dos ímpares*****\n")

input_list = input("Digite uma lista de números separados por espaço: ")

# Converte a entrada do usuário em uma lista de números  

input_list = [int(item) for item in input_list.split()]

# Cria duas listas vazias para armazenar os números p e í

list_pares = []
list_impares = []

# Percorre a lista de números e adiciona os números pares e ímp

for num in input_list:
    if num % 2 == 0:
        list_pares.append(num)
    else:
        list_impares.append(num)


print("\n-Lista de números pares:", list_pares)
print("-Lista de números ímpares:", list_impares)
print("-Lista com todos os números:", input_list)

print("\n*****Fim do programa*****")
