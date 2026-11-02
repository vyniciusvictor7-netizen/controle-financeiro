def normaliza_tipo(texto):
    texto = texto.strip().lower().replace('saida','saída')
    if texto == 'entrada' or texto == 'saída':
        return texto
    
    return None
