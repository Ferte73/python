from operator import truediv

def adicao(n1, n2):
    return int(n1) + int(n2)

def subtracao(n1, n2):
    return int(n1) - int(n2)

def divisao(n1, n2):
    return int(n1) / int(n2)

def multiplicacao(n1, n2):
    return int(n1) * int(n2)

while True:
    operacao = input("Utilizando apenas + para adição,\n- para subtração,\n* para multiplicação e\n/ para divisão.\n Qual operação deseja realizar? ")
    if operacao == "+":
        n1 = input("Quais números deseja adicionar?")
        n2 = input()
        print(adicao(n1, n2))
    
    elif operacao == "-":
        n1 = input("Quais números deseja subtrair?")
        n2 = input()
        print(subtracao(n1, n2))
    
    elif operacao == "*":
        n1 = input("Quais números deseja multiplicar?")
        n2 = input()
        print(multiplicacao(n1, n2))

    elif operacao == "/":
        n1 = input("Quais números deseja dividir?(numerador/denominador)?")
        n2 = input()
        print(divisao(n1, n2))
    
    else:
        break