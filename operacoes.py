# arquivo: operacoes.py

def cadastrar_bilhete(dicionario, codigo, tipo, saldo):
    dicionario[codigo] = {'tipo': tipo, 'saldo': saldo}

def recarregar_bilhete(dicionario, codigo, valor):
    if codigo in dicionario:
        dicionario[codigo]['saldo'] += valor
        print("Recarga realizada com sucesso!")
    else:
        print("Bilhete não encontrado.")

def acessar_transportes(dicionario, codigo, valor_passagem):
    if codigo in dicionario:
        if dicionario[codigo]['saldo'] >= valor_passagem:
            dicionario[codigo]['saldo'] -= valor_passagem
            print("Acesso autorizado!")
        else:
            print("Saldo insuficiente. Por favor, recarregue seu bilhete.")
    else:
        print("Bilhete não encontrado.")
