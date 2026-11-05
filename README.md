# Controle Financeiro

Ele serve para ter controle sobre suas finanças, anotar suas movimentações no mês seja elas: recebimento de salário, compras e afins.
Programa útil para pessoas que não têm controle sobre as suas finanças e gostariam de deixar salvo suas movimentações.

## Funcionalidades

- Abre um menu do Controle Financeiro com 9 funcionalidades.

### No menu

1. Cadastrar movimentação (Cadastrar movimentações de entrada e saída)
2. Listar movimentações (listar todas as suas movimentações com data e a hora em que foi feita)
3. Ver saldo (Mostra o seu saldo atual)
4. Ver resumo (Mostra todas as suas entradas, saídas e saldo)
5. Buscar movimentação (Busca uma movimentação pela descrição ou pelo tipo entrada ou saída)
6. Excluir movimentação (Exclui uma movimentação pela sua posição)
7. Filtrar movimentação por tipo (Filtra uma lista pelo tipo de movimentação entrada ou saída)
8. Editar movimentação (Edita uma movimentação podendo alterar sua descrição, valor e seu tipo)
9. Encerrar programa (Encerra o programa)

### Por trás do programa

- Os dados ficam armazenados em um JSON, para que você não perca nada ao fechar.
- Na hora do cadastro cada movimentação recebe a descrição, valor, tipo, data, hora e um ID para cada movimentação.
- Quando um arquivo está vazio ou estragado o programa abre sem erros, começando com uma lista vazia.
- Na opção 8 em Editar movimentação caso o usuário digite a tecla ENTER sem escrever nada o programa mantém a movimentação sem alterá-la. 

## Limitações do programa

- Quando o arquivo está estragado o programa começa sem avisar e o próximo cadastro grava por cima.
- O programa ainda não permite que cada pessoa tenha suas movimentações separadas.
- A data e a hora é definida a partir do momento que o usuário cadastra sua movimentação. 
- O programa ainda não permite filtrar por data e hora ou categoria.

## Como rodar

- Atualmente testado na versão do python 3.12
- Precisam estar na mesma pasta dados o arquivo CONTROLE_FINANCEIRO.PY, dados_e_calculos.py
- Para abrir o programa digite no terminal da pasta dados `python CONTROLE_FINANCEIRO.PY` se não funcionar tente `py CONTROLE_FINANCEIRO.PY`
- Os dados ficam guardados em um arquivo JSON com o nome: movimentacoes.json (ele é criado dentro da pasta onde o programa está rodando)

## O que aprendi

- Dividir funções para não repetir código.
- Usar try/except para evitar que o programa quebre.
- Guardar os dados de um jeito e mostrar de outro, por exemplo data e hora: No JSON: `2026-11-03 23:31:49` / na tela: `03/11/2026 23:31`
- Testar a cada mudança no programa.
- Separar em módulos para deixar o código mais limpo.