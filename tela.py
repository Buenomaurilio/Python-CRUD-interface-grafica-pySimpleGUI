import PySimpleGUIQt as sg 
from back import *

# Colunas da Tabela
header = ['Qtd', 'DataInicial', 'DataFinal', 'Vitrine']

# Criando o layout da Tela
layout = [
    [sg.Button('Buscar', size=(10,1)), sg.Button('Sair', size=(10,1))],
    [sg.Table('',key='dados_exclusiva', headings=header)]
]

# Instanciando a Tela 
janela = sg.Window('Nome Janela', layout, resizable=False, size=(550, 200))
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    if evento == 'Buscar':
        pass
        dados = responder()
        janela['dados_exclusiva'].update(dados)

janela.close()
