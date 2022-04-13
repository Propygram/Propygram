import requests
import json

authorization = 'OTA3Njg1NTErMTEyMjIzMjMz.YYtgki.2oAlIEkBy22CEu_htpOVyv6927fb' #<-- example
channelid = '367682373825396287' #<-- example

def write(tekst):
    try:
        payload = {
            'content': tekst
        }

        header = {
            'authorization': authorization
        }

        requests.post('https://discord.com/api/v9/channels/'+channelid+'/messages', data=payload, headers=header )
    except ConnectionError:
        print('Brak stabilnego łącza')

def read():
    global kontent_nowe

    try:
        header = {
            'authorization': authorization
        }

        r = requests.get('https://discord.com/api/v9/channels/'+channelid+'/messages?limit=50', headers=header )
        jsonn = json.loads(r.text)
        
        kontent_nowe = jsonn[0]['content']
        print(kontent_nowe)

    except:
        print('Wystąpił bład podczas odczytywania plików')
