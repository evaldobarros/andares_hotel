# funcão que calcula dois numeros 
def calculadora (numero1,numero2,operacao):
    if (operacao == "+"):
      resultado = numero1 + numero2
    elif (operacao == "-"):
      resultado = numero1 - numero2
    elif (operacao == "*"):
      resultado = numero1 * numero2
    else:
      resultado = numero1 / numero2
    return resultado
# declaraçao das variaveira, os dois numeros e a operaçao a ser execurada
numero1 = 10
numero2 = 20
operacao = "*"
print(numero1,operacao,numero2," = ",calculadora (numero1, numero2, operacao))