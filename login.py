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
        print(f"{Fore.RED}Erro: Sua senha deve conter no mínimo 8 digitos.{Style.RESET_ALL}")
        return False
    
    elif len(ints_list) < 1:
        print(f"{Fore.RED}Erro: Sua senha deve conter no mínimo 1 número.{Style.RESET_ALL}")
        return False

    elif len(upper_list) < 1:
        print(f"{Fore.RED}Erro: Sua senha deve conter no mínimo 1 letra maíuscula.{Style.RESET_ALL}")
        return False
    
    else:
        return True
        

def cadastro():
    os.system('cls')

    print(f"{Fore.CYAN}{'='*40}")
    print(f"{Fore.CYAN}           CADASTRO DE USUÁRIO")
    print(f"{Fore.CYAN}{'='*40}\n")

    try:
        with open("data.json", "r") as archive:
            data = json.load(archive)
    except FileNotFoundError:
        data = {"users": []}

    user = input("user: ")
    password = input("Password: ")

    ints_list, upper_list = splitpass(password)
    if strongpwrd(password, ints_list, upper_list) == True:

        for usuario in data["users"]:
            if usuario["user"] == user:
                print(f"{Fore.RED}Usuário já existe!{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")
                return

        new_user = {
            "user": user,
            "password": password
        }

        data["users"].append(new_user)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)

        print(f"{Fore.GREEN}Cadastrado com sucesso!{Style.RESET_ALL}")
        input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")
    else:
        input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")

def login():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{Fore.CYAN}{'='*40}")
    print(f"{Fore.CYAN}              LOGIN")
    print(f"{Fore.CYAN}{'='*40}\n")

    try:
        with open("data.json", "r") as loginfile:
            datalogin = json.load(loginfile)
    except FileNotFoundError:
        print(f"{Fore.RED}Arquivo de cadastros (data.json) não encontrado!{Style.RESET_ALL}")
        input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")
        return
    
    user = input(f"{Fore.YELLOW}user: {Style.RESET_ALL}")
    password = input(f"{Fore.YELLOW}Password: {Style.RESET_ALL}")

    encontrou = False

    for usuario in datalogin["users"]:
        if usuario["user"] == user and usuario["password"] == password:
            encontrou = True
            print(f"\n{Fore.GREEN}Você está logado!{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Bem-vindo, {user}!{Style.RESET_ALL}")
            input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")
            break

    if not encontrou:
        print(f"\n{Fore.RED}Usuário não encontrado, cadastre-se primeiro.{Style.RESET_ALL}")
        input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")



while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Fore.MAGENTA}{'='*40}")
    print(f"{Fore.MAGENTA}          SISTEMA DE LOGIN")
    print(f"{Fore.MAGENTA}{'='*40}\n")
    
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Cadastrar")
    print(f"{Fore.CYAN}2.{Style.RESET_ALL} Login")
    print(f"{Fore.CYAN}3.{Style.RESET_ALL} Sair")
    
    opcao = input(f"\n{Fore.YELLOW}Escolha uma opção: {Style.RESET_ALL}")

    if opcao == "1":
        cadastro()

    if opcao == "2":
        login()

    elif opcao == "3":
        print(f"\n{Fore.GREEN}👋 Até logo!{Style.RESET_ALL}")
        break

    else:
        print(f"\n{Fore.RED}Opção inválida!{Style.RESET_ALL}")
        input(f"{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")