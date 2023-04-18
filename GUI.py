from PySimpleGUI import PySimpleGUI as sg
from time import sleep

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuário', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', size=(20,1), password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de login', layout)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuário'] == 'extreme340' and valores['senha'] == '123456':
            print('Você está logado')
            sleep(0.5)
            break
