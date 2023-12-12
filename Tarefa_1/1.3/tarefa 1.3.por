programa {
  funcao inicio() {
    inteiro Auxiliar 
    inteiro array[3] 

    escreva("Digite três valores em lista desordenada: ")
    leia(array[0])
    leia(array[1])
    leia(array[2])

    para(inteiro i = 0; i <= 2; i++){
       para(inteiro j = 0; j <= 2; j++){
             se(array[i] < array[j]){
              Auxiliar = array[j]
              array[j] = array[i]
              array[i] = Auxiliar
             }
        }
    }

  escreva(array)
    
  }
}
