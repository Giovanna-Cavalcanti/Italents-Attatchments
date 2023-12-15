# . Elabore um programa que utilize um dicionário para simular a baixa de
# estoque das vendas de um supermercado. O programa deve realizar as
# seguintes validações:
# • Verificar se o produto está disponível no estoque.
# • Validar se o produto informado é válido.
# • Verificar se a quantidade solicitada está disponível no estoque.
# Ao final, o programa deve exibir para o cliente a quantidade de itens
# comprados e o valor total da compra.

# Dicionário com os produtos e seus respectivos preços

produtos = {
    "1": {"nome": "Arroz", "preco": 10.0},
    "2": {"nome": "Feijão", "preco": 8.0},
    "3": {"nome": "Macarrão", "preco": 5.0},
    "4": {"nome": "Óleo", "preco": 15.0},
    "5": {"nome": "Açúcar", "preco": 12.0},
    "6": {"nome": "Sal", "preco": 3.0},
    "7": {"nome": "Leite", "preco": 4.0},
}
# Dicionário com as quantidades disponíveis em estoque

estoque = {
    "1": 10,
    "2": 5,
    "3": 8,
    "4": 20,
    "5": 15,
    "6": 30,
    "7": 25,
}

# Dicionário com as quantidades compradas pelo cliente

compras = {
    "1": 2,
    "2": 3,
    "3": 0,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 4,
}

# Verifica se o produto está disponível no estoque

for codigo, quantidade in compras.items():
    if codigo not in produtos:
        print("Produto inválido:", codigo)
        continue
    if quantidade > estoque[codigo]:
        print("Quantidade insuficiente em estoque:", codigo)
        continue
# Calcula o valor total da compra
total = 0
for codigo, quantidade in compras.items():
    if codigo in produtos:
        total += quantidade * produtos[codigo]["preco"]

# Exibe o valor total da compra

print("\nValor total da compra: R$", total)
print("Quantidade de itens comprados:", sum(compras.values()))

      
