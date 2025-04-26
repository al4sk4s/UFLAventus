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

            return({"SearchID": div.get('value'), "Cookie":sessao.cookies})
        
        except Exception as e:
            print('Houve um erro no request')
            print(traceback.format_exc())

        #Retorna o valor do ID caso tenha
        #return {"SearchID":div.get("id"), "Cookie":sessao.cookies}
        return None
    
    def PostRequest(id, Cookie):
        try:
            sessao = requests.session()
            sessao.cookies.update(Cookie)
            payload = {"modulo_exportacao": id, "num_resultados": 1, "exportar_relatorio": "html"}
            response = sessao.post(main_url, data=payload).text

            print(response)

            # Parsear o HTML
            #soup = BeautifulSoup(response, 'html.parser')

            # Busca pela div que contenha o ID de pesquisa
            #div = soup.find("input", {'name':'modulo_exportacao'})

            #return(div.get('value'))
        
        except Exception as e:
            print('Houve um erro no request')
            print(traceback.format_exc())

        #Retorna o valor do ID caso tenha
        #return {"SearchID":div.get("id"), "Cookie":sessao.cookies}
        return None