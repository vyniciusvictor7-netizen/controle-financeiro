import json
from datetime import datetime
import uuid

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

lista_movimentacao = carregar_dados()

def adicionar_movimentacao(): 
    movimentacao = dict()
    movimentacao['Descricao'] = input('Descrição: ').strip().lower()
    valor = pedir_valor()
    tipo = validar()
    movimentacao['Valor'] = valor
    movimentacao['Tipo'] = tipo
    data = datetime.now()
    movimentacao['DataHora'] = data.strftime('%Y-%m-%d %H:%M:%S')
    movimentacao['ID'] = str(uuid.uuid4())
    lista_movimentacao.append(movimentacao)
    salvar_dados(lista_movimentacao)

def pedir_valor():
    while True:
        try:
            valor = float(input('Digite o valor: ').replace(',','.'))
            if valor <= 0:
                print('\nDigite um valor maior que 0.')
            else:
                return valor
        except ValueError:
            print('\nValor invalido! Digite apenas numeros.\n')
            
def filtrar_por_tipo():
    if not lista_movimentacao:
        print('\nNenhuma movimentação cadastrada.')
        return
    filtro = normaliza_tipo(input('\nFiltrar lista por - [ENTRADA] / [SAÍDA]: '))
    while filtro is None:
        filtro = normaliza_tipo(input('\nOpção inválida. Digite [ENTRADA] / [SAÍDA]: '))
    encontrou = False

    for i, mov in enumerate(lista_movimentacao, start=1):
        if mov['Tipo'] == filtro:
            mostrar_movimentacao(i,mov)
            encontrou = True
    if not encontrou:
        print('\nNenhuma movimentação encontrada.')


def buscar_movimentacao():
    if not lista_movimentacao:
        print('\nNenhuma movimentação cadastrada.')
        return
    pesquisa = input('\nDigite a descrição exata ou o tipo: ').strip().lower()
    while not pesquisa:
        pesquisa = input('\nDigite a descrição exata ou o tipo: ').strip().lower()
    tipo_pesquisado = normaliza_tipo(pesquisa)
    encontrou = False

    for i, mov in enumerate(lista_movimentacao, start=1):
        if pesquisa == mov['Descricao'] or tipo_pesquisado == mov['Tipo']:
            mostrar_movimentacao(i,mov)
            encontrou = True
    if not encontrou:
        print('\nNenhuma movimentação encontrada.')
        
def excluir_movimentacao():
    if not lista_movimentacao:
        print('\nNenhuma movimentação cadastrada.')
        return
    listar_movimentacoes() 
    remover = pedir_posicao('\nQual movimentação voce quer remover: ')
    lista_movimentacao.pop(remover - 1)
    salvar_dados(lista_movimentacao)
    print('\nMovimentação removida com sucesso')     
    
def pedir_posicao(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 1 or numero > len(lista_movimentacao):
                print('\nEssa movimentação não existe')
                print('\nDigite novamente')
            else:
                return numero    
        except ValueError:
                print('\nOpção não existe digite novamente.')

def editar_movimentacao():
    if not lista_movimentacao:
        print('\nNenhuma movimentação cadastrada.')
        return
    listar_movimentacoes()
    posicao = pedir_posicao('\nQual movimentação voce deseja editar: ')
    nova_descricao = input('\nDigite a nova descrição: ').strip().lower()
    if not nova_descricao:
        print('\nA descrição não foi alterada.')
    else:
        lista_movimentacao[posicao - 1]['Descricao'] = nova_descricao
        salvar_dados(lista_movimentacao)
        print('\nEdição concluída!')    
    while True:
        try:
            novo_valor = input('\nDigite o novo valor: ').strip().replace(',','.')
            if not novo_valor:
                print('\nO valor não foi alterado.')
                break
            else:
                float_valor = float(novo_valor)
                if float_valor <= 0:
                    print('\nDigite um valor maior que 0')
                else:
                    lista_movimentacao[posicao -1]['Valor'] = float_valor
                    print('\nValor alterado.')
                    salvar_dados(lista_movimentacao)
                    break
        except ValueError:
            print('\nDigite um número válido.')
    while True:
        novo_tipo = input('\nDigite o novo tipo: ').strip()
        if not novo_tipo:
            print('\nO tipo não foi alterado.')
            break
        else:
            novo_tipo = normaliza_tipo(novo_tipo)
            while novo_tipo is None:
                print('\nTipo inválido.')
                novo_tipo = normaliza_tipo(input('\nDigite Entrada ou Saída: '))
            lista_movimentacao[posicao - 1]['Tipo'] = novo_tipo
            salvar_dados(lista_movimentacao)
            print('\nO tipo foi alterado.')
            break

def normaliza_tipo(texto):
    texto = texto.strip().lower().replace('saida','saída')
    if texto == 'entrada' or texto == 'saída':
        return texto
    
    return None

def validar():    
    tipo = normaliza_tipo(input('Tipo: '))
    while tipo is None:
        print('Tipo inválido')
        tipo = normaliza_tipo(input('Digite Entrada ou Saída: '))
    return tipo

def mostrar_movimentacao(numero, mov):
    data = datetime.strptime(mov["DataHora"], "%Y-%m-%d %H:%M:%S")
    data_br = data.strftime("%d/%m/%Y %H:%M")
    print(f'{numero}. {mov["Descricao"]} - R$ {mov["Valor"]:.2f} - {mov["Tipo"].capitalize()} - {data_br}')

def listar_movimentacoes():
    if not lista_movimentacao:
        print('\nNenhuma movimentação cadastrada.')
    else:
        print('\n===== MOVIMENTAÇÕES =====\n')
        for i, mov in enumerate(lista_movimentacao, start = 1):
            mostrar_movimentacao(i,mov)

def calcular_totais():
    entradas = 0
    saidas = 0
    for n in (lista_movimentacao):
        if n['Tipo'] == 'entrada':
            entradas += n['Valor']
        elif n['Tipo'] == 'saída':
            saidas += n['Valor']   
    return entradas, saidas
        
def saldo_total():
    entradas, saidas = calcular_totais()
    saldo = entradas - saidas
    return f'\nR$: {saldo:.2f}'

def resumo():
    print('\n===== RESUMO =====\n')
    entradas, saidas = calcular_totais()
    print(f'Total de entradas: R$ {entradas:.2f}')
    print(f'Total de saídas: R$ {saidas:.2f}')
    print(saldo_total())

def encerrar():
    print('\nPrograma encerrado.\n')        


menu = '''
\n===== CONTROLE FINANCEIRO =====\n
1 - Adicionar movimentação
2 - Listar movimentações
3 - Ver saldo
4 - Ver resumo
5 - Buscar movimentação
6 - Excluir movimentação
7 - Filtrar movimentação por tipo
8 - Editar movimentação
9 - Encerrar programa

Escolha uma opção: '''
while True:
    try:
        opcao = int(input(menu))
    except ValueError:
        print('\nDigite um número válido!')
        continue
    
    if opcao == 1:
        adicionar_movimentacao()      
    elif opcao == 2:
        listar_movimentacoes()
    elif opcao == 3:
        print(saldo_total())
    elif opcao == 4:
        resumo()
    elif opcao == 5:
        buscar_movimentacao()
    elif opcao == 6:
        excluir_movimentacao()
    elif opcao == 7:
        filtrar_por_tipo()
    elif opcao == 8:
        editar_movimentacao()
    elif opcao == 9:
        encerrar()
        break
    else:
        print('\nOpção inválida')
    