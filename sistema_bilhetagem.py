# arquivo: sistema_bilhetagem.py

# Importa a biblioteca colorama para fornecer cores no terminal
import colorama
from colorama import Fore, Back, Style
import datetime  # Importa a biblioteca datetime

# Inicializa a biblioteca colorama para que as cores sejam automaticamente resetadas após cada uso
colorama.init(autoreset=True)

from operacoes import *

# Tabela de valores dos bilhetes
tabela_bilhetes = {
    '1': {'tipo': 'Bilhete Comum', 'valor': 5.00},
    '2': {'tipo': 'Bilhete Estudante', 'valor': 2.50},
    '3': {'tipo': 'Bilhete Idoso', 'valor': 1.25}
}

# Dicionário para armazenar os bilhetes e seus saldos
bilhetes = {}

# Função para imprimir uma linha de separação
def lin():
    print(Fore.YELLOW + '--'*30)

# Função para mostrar o menu principal do sistema
def mostrar_menu():
    lin()
    print(Fore.GREEN + "\n             SISTEMA DE BILHETAGEM ELETRONICA")
    print(Fore.GREEN + "                      BEM VINDO(A)!!\n")
    lin()
    print(Fore.GREEN + "(1) ------- Cadastrar Bilhete")
    print(Fore.GREEN + "(2) ------- Recarregar Bilhete")
    print(Fore.GREEN + "(3) ------- Pagar Passagem")
    print(Fore.GREEN + "(4) ------- Historico de Recarga")
    print(Fore.GREEN + "(0) ------- Sair")
    lin()
    lin()

# Função para mostrar as opções de bilhetes disponíveis para cadastro
def mostrar_opcoes_bilhetes():
    print("\nOpções de Bilhetes:")
    for codigo, bilhete in tabela_bilhetes.items():
        print(Fore.GREEN + f"Código: {codigo}, Tipo: {bilhete['tipo']}, Valor: R${bilhete['valor']:.2f}")

# Função para cadastrar um novo bilhete
def cadastrar_bilhete():
    mostrar_opcoes_bilhetes()
    codigo_bilhete = input("Digite o código do bilhete desejado: ")
    if codigo_bilhete in tabela_bilhetes:
        bilhetes[int(codigo_bilhete)] = tabela_bilhetes[codigo_bilhete]['valor']  # Armazena o código do tipo de bilhete
        print("Bilhete cadastrado com sucesso!")
    else:
        print("Código de bilhete inválido.")

# Função para recarregar o saldo de um bilhete existente
def recarregar_bilhete():
    codigo_bilhete = input("Digite o código do bilhete para recarregar: ")
    if int(codigo_bilhete) in bilhetes:
        valor_recarga = float(input("Digite o valor da recarga: "))
        bilhetes[int(codigo_bilhete)] += valor_recarga  # Atualiza o saldo do bilhete com o valor da recarga
        # Obtém a data e hora atuais
        data_hora_atual = datetime.datetime.now()
        # Formata a data e hora atual para exibição
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Recarga realizada com sucesso em {data_hora_formatada}!")
    else:
        print(Fore.RED + "Bilhete não encontrado! Por favor, cadastre-o antes.")

# Função para pagar a passagem com o saldo de um bilhete
def pagar_passagem():
    codigo_bilhete = input("Digite o código do bilhete para pagar a passagem: ")
    if int(codigo_bilhete) in bilhetes:
        saldo_bilhete = bilhetes[int(codigo_bilhete)]
        if saldo_bilhete > 0:  # Verifica se há saldo suficiente
            valor_passagem = tabela_bilhetes[codigo_bilhete]['valor']
            if valor_passagem <= saldo_bilhete:  # Verifica se há saldo suficiente para pagar a passagem
                bilhetes[int(codigo_bilhete)] -= valor_passagem
                # Obtém a data e hora atuais
                data_hora_atual = datetime.datetime.now()
                # Formata a data e hora atual para exibição
                data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
                print(f"Passagem paga com sucesso em {data_hora_formatada}!")
                print(f"Saldo atual do bilhete: R${bilhetes[int(codigo_bilhete)]:.2f}")
            else:
                print(Fore.RED + "Saldo insuficiente. Por favor, recarregue seu bilhete.")
        else:
            print("Bilhete não foi recarregado. Por favor, recarregue seu bilhete antes de pagar a passagem.")
    else:
        print(Fore.RED  + "Bilhete não encontrado!")

# Função para exibir o histórico de recargas dos bilhetes
def historico():
    print("\nVerificar historico de recargas: ")
    for codigo, saldo in bilhetes.items():
        tipo_bilhete = tabela_bilhetes[str(codigo)]['tipo']
        print(f"Código: {codigo}, Tipo: {tipo_bilhete}, Saldo: R${saldo:.2f}")

# Função principal que controla o fluxo do programa
def main():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            cadastrar_bilhete()

        elif opcao == '2':
            recarregar_bilhete()

        elif opcao == '3':
            pagar_passagem()

        elif opcao == '4':
            historico()

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print(Fore.RED + "Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
