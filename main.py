from gtts import gTTS
from playsound import playsound
import PySimpleGUI as sg


def tela_inicial():
    layout = [
        [sg.Text('transformando texto em áudio')],
        [sg.Text('nome do arquivo')],
        [sg.Input(key='nome')],
        [sg.Text('texto a ser gerado')],
        [sg.Input(key='texto')],
        [sg.Button('gerar áudio')],
        [sg.Text('', key='msg')]
    ]
    return sg.Window('transformando texto em áudio', layout=layout, finalize=True)


telaInicial = tela_inicial()

while True:
    window, eeventos, valores = sg.read_all_windows()
    if eeventos == sg.WIN_CLOSED:
        break
    if valores['nome'] == '' or valores['texto'] == '':
        window['msg'].update('todos os campos devem ser preenchidos')
    elif valores['nome'] != '' or valores['texto'] != '':
        window['msg'].update('')
    if window == telaInicial and eeventos == 'gerar áudio':

        audio = valores['nome'] + '.mp3'

        linguagem = 'pt-br'

        sp = gTTS(

            text=valores['texto'],
            lang=linguagem
        )
        sp.save(audio)
        playsound(audio)
