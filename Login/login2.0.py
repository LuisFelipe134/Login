usuarios = {}
def menu():
    print("\nMENU")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

def cadastro():
   usuario = input("Digite o usuario: ")
   senha = input("Digite a senha: ")
   usuarios[usuario] = senha
   print("Cadastro realizado com sucesso!")


def login():
    usuario = input("Digite o usuario: ")
    senha = input("Digite a senha: ")
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Login invalido!")


while True:
    menu()

    op = input("Escolha: ")

    if op == "1":
        cadastro()

    elif op == "2":
        login()
    
    elif op == "3":
        break