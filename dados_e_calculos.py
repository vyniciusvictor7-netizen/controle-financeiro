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