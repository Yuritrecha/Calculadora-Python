nome_usuario =  input("Digite seu nome: ")

print ("Bem vindo {} ".format(nome_usuario))

def calcular():
    operador = input('''
Por favor, adicione um operador :
+ for Adição
- for Subtração
* for Multiplication
/ for Divisão
''')

    num1 = int(input("Digite um número: "))
    num2 = int(input ("Digite outro número: "))

    if operador == "+":
        #Adiçao
        print('{} + {} = '.format(num1, num2))
        print (num1 + num2)

    elif operador == "-":
        #Subtração
        print('{} - {} = '.format(num1, num2))
        print (num1 - num2)

    elif operador == "*":
        #Multiplicação
        print('{} * {} = '.format(num1, num2))
        print (num1 * num2)

    elif operador == "/":
        #Divisão
        print('{} / {} = '.format(num1, num2))
        print (num1 / num2)

    else:
        print("Você digitou um operador inválido.")

calcular()

def reiniciar():
    calc_reiniciar = input("Você deseja calcular novamente? Digite S para SIM ou N para NÃO")

    if calc_reiniciar.upper == "Y":
        calcular()

    elif calc_reiniciar.upper == "N":
        print('Até a próxima.')

    else:
        calc_reiniciar()

