import time
import traceback
from utils import *

"""
url importantes:
https://sig.ufla.br/modulos/publico/eventos/index.php?xml=1
https://sig.ufla.br/webservice/busca.xml.php?id=[id]&busca=[nome]
"""

def main():
    while True:
        try:
            #primeiro passo do request, conseguir o ID
            SearchID = GetRequest.GetSearchID()
            if SearchID == None:
                return
            
            print(SearchID)
            #segundo passo do request, fazer a pesquisa dos cursos
            SearchResult = SearchRequest.Search(SearchID)
            
            print(SearchResult)
        
        except Exception as e:
            print('Houve um erro ao executar, tentando novamente...')
            print(traceback.format_exc())

        time.sleep(300)      


if __name__ == "__main__":
    main()