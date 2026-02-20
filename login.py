from colorama import Fore, Style
import json
import os


def splitpass(password):
    ints_list = [x for x in password if x.isdigit()]

    upper_list = [x for x in password if x.isupper()]

    return ints_list, upper_list

def strongpwrd(password, ints_list, upper_list):
    splitpass(password)

    if len(password) < 8:
        print("Erro: Sua senha deve conter no mínimo 8 digitos.")
        return False
    elif len(ints_list) < 1:
        print("Erro: Sua senha deve conter no mínimo 1 número.")
        return False

    elif len(upper_list) < 1:
        print("Erro: Sua senha deve conter no mínimo 1 letra maíuscula.")
        return False
    
    else:
        return True
        

def cadastro():
    try:
        with open("data.json", "r") as archieve:
            data = json.load(archieve)
    except FileNotFoundError:
        data = {"users": []}

    user = input("user: ")
    password = input("Password: ")
    ints_list, upper_list = splitpass(password)
    if strongpwrd(password, ints_list, upper_list) == True:

        for usuario in data["users"]:
            if usuario["user"] == user:
                print("Usuário já existe!")
                input("Pressione ENTER para continuar...")
                return

        new_user = {
            "user": user,
            "password": password
        }

        data["users"].append(new_user)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)

        print("Cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")

def login():
    os.system('cls')

    print("Sign-in\n")
    try:
        with open("data.json", "r") as loginfile:
            datalogin = json.load(loginfile)
    except FileNotFoundError:
        print("Cadastro não encontrado!")
        input("Pressione ENTER para continuar...")
        return
    
    user = input("user: ")
    password = input("Password: ")

    encontrou = False

    for usuario in datalogin["users"]:
        if usuario["user"] == user and usuario["password"] == password:
            encontrou = True
            print("Você está logado!")
            input("Pressione ENTER para continuar...")
            break

    if not encontrou:
        print("Usuário não encontrado, cadastre-se primeiro.")
        input("Pressione ENTER para continuar...")



while True:
    os.system('cls')
    print("MENU DE ESCOLHAS\n")
    print("1. Cadastrar")
    print("2. Login")
    print("3. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastro()

    if opcao == "2":
        login()

    if opcao == "3":
        break