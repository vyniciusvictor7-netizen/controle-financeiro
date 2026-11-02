import json

def carregar_dados():
    try:
        with open('movimentacoes.json', 'r', encoding= 'utf-8') as arquivo:
            ler = json.load(arquivo)
            return ler
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(lista):
    with open ('movimentacoes.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)
        
def normaliza_tipo(texto):
    texto = texto.strip().lower().replace('saida','saída')
    if texto == 'entrada' or texto == 'saída':
        return texto
    
    return None

def calcular_totais(lista):
    entradas = 0
    saidas = 0
    for n in (lista):
        if n['Tipo'] == 'entrada':
            entradas += n['Valor']
        elif n['Tipo'] == 'saída':
            saidas += n['Valor']   
    return entradas, saidas

def saldo_total(lista):
    entradas, saidas = calcular_totais(lista)
    saldo = entradas - saidas
    return saldo