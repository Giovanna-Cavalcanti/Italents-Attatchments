programa {
  funcao inicio() {
    real Valor, Desconto, ValorTotal

    escreva("Digite o valor do produto: ")
    leia(Valor)

    Desconto = (Valor * 10)/100

    ValorTotal = Valor - Desconto

    escreva("\nO valor do seu produto com 10% de desconto é: ", ValorTotal, "R$\n")
  }
}
