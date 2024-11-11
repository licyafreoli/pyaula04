def pares (lista):
    
    for numero in lista:
        if numero%2==0:
            print(numero)
aleatorio=input("Digite os números separados por espaço: ")

aleatorio = [int(num) for num in aleatorio.split()]

pares(aleatorio)