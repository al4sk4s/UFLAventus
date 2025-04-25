import traceback
import requests
from bs4 import BeautifulSoup

class ListRequest():
    def __init__(self):
        pass

    global main_url; main_url = "https://sig.ufla.br/modulos/publico/eventos/index.php"

    def GetSearchID():
        try:
            sessao = requests.session()
            response = sessao.get(main_url).text

            # Parsear o HTML
            soup = BeautifulSoup(response, 'html.parser')

            # Busca pela div que contenha o ID de pesquisa
            div = soup.find("input", {'name':'modulo_exportacao'})

            print(div.get('value'))
        
        except Exception as e:
            print('Houve um erro no request')
            print(traceback.format_exc())
            return None

        #Retorna o valor do ID caso tenha
        #return {"SearchID":div.get("id"), "Cookie":sessao.cookies}
        return