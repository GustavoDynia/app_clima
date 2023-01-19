import requests
from pprint import pprint
from time import sleep
from tkinter import *

control =''
datalist = dict()  #dicionário com informações aproveitadas da API, que de fato aparecem no meu programa.

while True:
    control = input('Deseja saber o clima em alguma cidade? [S]sim ou [X] para encerrar o programa: ').upper().strip()
    if control == 'X':
        print('Encerrando o programa...')
        sleep(1)
        print('Programa encerrado. Volte sempre!')
        break
    cidade = input('Digite o nome da cidade ou [X] para encerrar o programa: ').capitalize().strip()

    if cidade == 'X':
        print('Encerrando o programa...')
        sleep(1)
        print('Programa encerrado. Volte sempre!')
        break

    else:
        API_Chave = 'c8fb29305cba491d93701657221712'
        base_URL = 'http://api.weatherapi.com/v1/current.json?key='+API_Chave+'&q='+cidade+'&aqi=no'   #URL BASE + KEY_API + "&q=" + CIDADE + "&aqi=no"
        dados_do_tempo = requests.get(base_URL).json()  #VAR RECEBENDO COMANDO DE REQUISIÇÃO DE DADOS DA API DO URL EM FORMATO JSON
        #AQUI TERMINA O CÓDIGO DA CONEXÃO COM API


        dado_tratado = dados_do_tempo.copy()

        def tratar_data():
            '''
            Converte o formato de data YYYY/MM/DD para DD/MM/YYYY
            :return: dia+mes+ano
            '''
            dia = dado_tratado['location']['localtime'][8:10]
            mes = dado_tratado['location']['localtime'][4:8]
            ano = dado_tratado['location']['localtime'][:4]
            datatratada = dia+mes+ano
            return datatratada
        datatratada = tratar_data()

        print('-' * 100)
        print(f'''Local: {dado_tratado['location']['name'].capitalize()}, {dado_tratado['location']['region']}, {dado_tratado['location']['country']}\nData: {datatratada}\nHora local: {dado_tratado['location']['localtime'][11:]}''')
        print('-'*100)

        datalist['Temperatura'] = f'{dado_tratado["current"]["temp_c"]}C°'
        datalist['Sensação Térmica'] = f'{dado_tratado["current"]["feelslike_c"]}C°'
        datalist['Vento'] = f'{dado_tratado["current"]["gust_kph"]}km/h'
        datalist['Nuvens'] = f'{dado_tratado["current"]["cloud"]}%'
        datalist['Umidade'] = f'{dado_tratado["current"]["humidity"]}%'
        datalist['Última checagem'] = f'{dado_tratado["current"]["last_updated"]}'

        for c, d in datalist.items():
            print(f'{c:<16} {d.center(6)}')

        sleep(2)
        print('-'*100)
        #print(dados_do_tempo)
        '''janela = Tk()
        janela.title('Clima Tempo')
        texto_orientacao = Label(janela, text='Texto de teste')
        texto_orientacao.grid(column=0, row=0)
        janela.mainloop()'''