def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por 0!"
    else:
        return a / b
    
def exponenciacao(a, b):
    return a**b

def porcentagem(a, b):
    return a * (b / 100)

while True:
    print("\n===== Calculadora =====")
    print("\n1 - Soma")
    print("\n2 - Subtração")
    print("\n3 - Multiplicação")
    print("\n4 - Divisão")
    print("\n5 - Exponenciação")
    print("\n6 - Porcntagem total/porcentagem")
    print("\n0 - Sair")
    
    opcao = int(input("\nEscolha uma opção: "))
    
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))
    
    if opcao == 1:
        resultado = soma(num1, num2)
        print(f"\nResultado: {resultado}")
    elif opcao == 2:
        resultado = subtracao(num1, num2)
        print(f"\nResultado: {resultado}")
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
        print(f"\nResultado: {resultado}")
    elif opcao == 4:
        resultado = divisao(num1, num2)
        print(f"\nResultado: {resultado}")
    elif opcao == 5:
        resultado = exponenciacao(num1, num2)
        print(f"\nResultado: {resultado}")
    elif opcao == 6:
        resultado = porcentagem(num1, num2)
        print(f"\nResultado: {resultado}")
    elif opcao == 0:
        break
    else:
        print("\nEscolha uma opção válida!")