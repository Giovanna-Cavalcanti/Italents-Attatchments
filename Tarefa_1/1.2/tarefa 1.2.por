programa {
  funcao inicio() {
    real Celsius, Fahrenheit

    escreva("Digite um valor em graus celsius: ")
    leia(Celsius)

    Fahrenheit = (Celsius * 9/5)+32

    escreva("\n-> O valor de ", Celsius, " graus celsius equivale a: ", Fahrenheit, " graus fahrenheit\n")
  }
}
