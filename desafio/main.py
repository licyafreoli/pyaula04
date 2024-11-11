def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    return "Erro! Divisão por zero."

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        opcao = input("Digite o número da operação: ")
        
        if opcao == '5':
            print("Saindo...")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == '1':
            print(f"O resultado da soma é: {somar(num1, num2)}")
        elif opcao == '2':
            print(f"O resultado da subtração é: {subtrair(num1, num2)}")
        elif opcao == '3':
            print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
        elif opcao == '4':
            print(f"O resultado da divisão é: {dividir(num1, num2)}")
        else:
            print("Opção inválida!")

calculadora()
