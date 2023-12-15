print("\n******Digite sete valores sem repetir, e eles serão mostrados na tela em"
        " ordem crescente******\n")

lista = []

for i in range(7):
    valor = int(input("\nDigite o %dº valor: " % (i+1)))
    lista.append(valor)

lista.sort()

# a lista não pode ter valores repetidos, para deletar os valores
#repetidos, basta usar o comando "set"

list = set(lista)
      
print("\nValores em ordem crescente e sem repetir: ", list)
