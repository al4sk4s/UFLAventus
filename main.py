import time
import traceback
from utils import *

"""
url importantes:
https://sig.ufla.br/modulos/publico/eventos/index.php?xml=1
https://sig.ufla.br/webservice/busca.xml.php?id=[id]&busca=[nome]

modulo_exportacao: 568b7107a527eec34b61942d5bcbec9b
num_resultados: 206
exportar_relatorio: html
token_csrf: dbb2feaa6cb7b798b2a5022d7b2d4e87f351fc166ccc6276eddd7cd51091e08d

https://sig.ufla.br/modulos/publico/eventos/index.php

<input type="hidden" name="token_csrf" value="dbb2feaa6cb7b798b2a5022d7b2d4e87f351fc166ccc6276eddd7cd51091e08d">

neero, neesa, neeitech
"""

def main():
    while True:
        try:
            #primeiro passo do request, conseguir o ID
            search_id = ListRequest.GetSearchID()
            
            if search_id == None:
                return
            
            ListRequest.PostRequest(search_id["SearchID"], search_id["Cookie"])

        
        except Exception as e:
            print('Houve um erro ao executar, tentando novamente...')
            print(traceback.format_exc())

        time.sleep(10)

if __name__ == "__main__":
    print('Iniciando...')
    main()