numeroCorreto = False
while (numeroCorreto == False):
   print("Insira seu nome e o ano de nacimento entre 1922 e 2021.")
   try:
       ano = int(input())
       nome = str(input())
       if ano >= 1922 and ano <= 2021:
           idade = 2022 - ano
           print("Você tem: ", idade, "anos")
           numeroCorreto = True
       else :
           print("Fora do ano permitido")
   except:
       print("Caracter inválido, digite novamente")
