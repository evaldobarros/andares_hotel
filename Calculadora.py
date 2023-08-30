# função calculadora 
def calculadora(num1, num2, operacao):
  if   (operacao == 1):
    resultado = primeiro_num + segundo_num
    operador = "+"
  elif (operacao == 2):
    resultado = primeiro_num - segundo_num
    operador = "-"
  elif (operacao == 3):
    resultado = primeiro_num * segundo_num
    operador = "*"
  else:
    resultado = int(primeiro_num) / int(segundo_num)
    operador = "/"
  return resultado,operador

# entrada dos dados
saida = False
while (saida == False):
  #entrada dos dados (menu na tela)
  print('           ') # pula linha
  print("                  Calculadora")
  print("             Escolha a operação: ")
  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")
  print("0: Sair ")
  try:
    print('               ') # pula linha
    operacao = int(input("Digite a opção: "))
    print("         ") # pula linha
    if (operacao == 0):
      saida = True
    elif (operacao >= 1) and (operacao <=4):
      primeiro_num = int (input("Escreva o primeiro termo: "))
      segundo_num  = int (input("Escreva o segundo termo: "))

#saida de dados com as respostas 
      resposta = calculadora (primeiro_num, segundo_num, operacao)  # chama a função com os valores para a operação
      print("o sesultada da operação escolhida", primeiro_num, resposta[1], segundo_num, " = ", resposta[0])
      print("                ") # pula linha
      print("Deseja continuar?  S/N")
      continuar= input()
      if (continuar == "S" or continuar == "s"):
        saida = False
      elif (continuar == "N" or continuar == "n"):
        saida = True
    else:
      print("Essa opção não existe” volte ao menu de opções")
  except:
    print("Essa opção não existe, voltar ao menu de opções")
print("              Fim da operação")