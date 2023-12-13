valor = float(input("\nInsira o valor em reais que deseja converter: "))

print("\nInsira a moeda desejada - D para dólar, E para euro, L para libra, " 
      "DC para dólar canadense, PA para peso argentino e PC para peso chileno:  ")

moeda = input()

if moeda == "D":
  print( valor,"Reais em dólar na data 13/12/2023 são: ", valor / 4.92, "USD")
elif moeda == "E":
  print( valor,"Reais em Euros na data 13/12/2023 são: ", valor / 5.35, "EUR")
elif moeda == "L":
  print( valor,"Reais em Libras na data 13/12/2023 são: ", valor / 6.23, "GBP")
elif moeda == "DC":
  print( valor,"Reais em Dólar Canadense na data 13/12/2023 são: ", valor / 3.64, "CAD")
elif moeda == "PA":
  print( valor,"Reais em Peso Argentino na data 13/12/2023 são: ", valor * 0.0061, "ARS")
elif moeda == "PC":
  print( valor,"Reais em Peso Chileno na data 13/12/2023 são: ", valor * 176.76, "CLP")
else: 
  print( "Moeda não reconhecida")
