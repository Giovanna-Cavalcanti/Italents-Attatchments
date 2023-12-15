# Desenvolva um programa que solicite ao usuário o nome, ano de 
# nascimento e número da carteira de trabalho (CTPS), armazenando essas 
# informações em um dicionário. Caso a CTPS informada seja diferente de
# zero, o programa deve solicitar o ano de contratação e o salário do 
# funcionário.
# Com base nas informações coletadas, o programa deve calcular e 
# acrescentar, no dicionário, a idade do funcionário e com quantos anos ele 
# irá se aposentar. Considere que o trabalhador deve contribuir por 35 anos 
# para se aposentar.
# Ao final, o programa deve exibir o conteúdo completo do dicionário, 
# incluindo os dados pessoais, profissionais e o cálculo da aposentadoria.

usuario = {}
usuario['nome'] = str(input('\nNome: '))
usuario['ano'] = int(input('\nAno de nascimento: '))
usuario['ctps'] = int(input('\nNúmero da carteira de trabalho: '))
usuario['idade'] = 2023 - usuario['ano']

if usuario['ctps'] != 0:
  usuario['ano_contratacao'] = int(input('\nAno de contratação: '))
  usuario['salario'] = float(input('\nSalário: R$'))
  usuario['idade'] = 2023 - usuario['ano']
  usuario['aposentadoria'] = 35 - (2023 - usuario['ano_contratacao'])

print('\n' + '-' * 50)
print(f'\nNome: {usuario["nome"]}')
print(f'\nIdade: {usuario["idade"]}')
print(f'\nCTPS: {usuario["ctps"]}')
if usuario['ctps'] != 0:
  print(f'\nAno de contratação: {usuario["ano_contratacao"]}')
  print(f'\nSalário: R${usuario["salario"]}')
  print(f'\nAposentadoria: {usuario["aposentadoria"]} anos')
  
