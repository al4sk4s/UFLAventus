import requests
import traceback
from bs4 import BeautifulSoup

class GetRequest:
    def __init__(self):
        print('get_request carregada')

    #conseguir o ID de pesquisa
    def GetSearchID():
        main_url = "https://sig.ufla.br/modulos/publico/eventos/index.php?xml=1"

        try:
            response = requests.get(main_url).text

            # Parsear o HTML
            soup = BeautifulSoup(response, 'html.parser')

            # Busca pela div que contenha o ID de pesquisa
            div = soup.find("div", class_="info_aguarde_sugestao")
        
        except Exception as e:
            print('Houve um erro no request')
            print(traceback.format_exc())
            return None

        #Retorna o valor do ID caso tenha
        return div.get("id")