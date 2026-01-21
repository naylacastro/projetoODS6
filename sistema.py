usuarios = []
consumos = []

# ------MENU PRINCIPAL------
def mostrar_menu():
    print("Contole de Consumo de Água")
    print("1 - Cadastrar Usuário")
    print("2 - Registrar Consumo de Água")
    print("3 - Ver Consumo Registrado")
    print("4 - Calcular Consumo Total")
    print("5 - Ver Alerta de Consumo")
    print("6 - Sair")

def menu():
    opcao = 0

    while opcao != 6:
        mostrar_menu()
        opcao = int(input("Escolha uma opção abaixo:"))

        if opcao == 1:
            print("Cadastrar usuário")

        elif opcao == 2:
            print("Registar consumo de água")

        elif opcao == 3:
            print("Ver consumo")

        elif opcao == 4:
            print("Calcular o consumo total")

        elif opcao == 5:
            print("Ver alerta de consumo")

        elif opcao == 6:
            print("Saindo do sistema.....")

        else:
            print("Opção inválida")

#    ------FUNÇÕES DO MENU-------

# 1 - Cadastrar usuário
def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    usuarios.append(nome)
    print(nome + " cadastrado!")


# 3 - Ver consumos registrados
def ver_consumo():
    if len(consumos) == 0:
        print("Nenhum consumo registrado.")
        return
    print("Consumos registrados:")
    for c in consumos:
        print(c)

 