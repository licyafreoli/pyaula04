def saudacao(hora):
    if 5 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    elif 18 <= hora < 24 or 0 <= hora < 5:
        print("Boa noite!")
    else:
        print("Hora inválida! Digite um valor entre 0 e 23.")

hora = int(input("Digite a hora atual (0-23): "))
saudacao(hora)
