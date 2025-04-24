import requests
import traceback
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

class SearchRequest():
    def __init__(self):
        pass

    def Search(SearchID, Cookie):
        search = input('Digite o termo de busca ')
        main_url = f"https://sig.ufla.br/webservice/busca.xml.php?id={SearchID}&busca={search}"

        try:
            sessao = requests.session()
            sessao.cookies.update(Cookie)
            response = sessao.get(main_url)

            root = ET.fromstring(response.content)

            for child in root:
                print(f"{child.tag}: {child.text}")
            
            if len(root) != 0: return True

        except Exception as e:
            print('Houve um erro no request')
            print(traceback.format_exc())
        
        return False