from requests.models import Response
import dados_token
import requests

class Previsao:

    def __init__(self):
        self.__cidade = '3694'
        self.__previsao_momento = self.transforma_json(self.consulta_momento())
        self.__previsao_momento_bruto = self.transforma_text(self.consulta_momento())
        self.__previsao_dia = self.transforma_json(self.consulta_dia())
        self.__previsao_dia_bruto = self.transforma_text(self.consulta_dia())

    def consulta_momento(self):
        url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + self.__cidade + "/current?token=" + dados_token.token()
        response1 = requests.get(url)
        return response1

    def consulta_dia(self):
        url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + self.__cidade + "/hours/72?token=" + dados_token.token()
        response2 = requests.get(url)
        return response2

    def transforma_json(self, dados):
        response_json = dados.json()
        return response_json
    
    def transforma_text(self, dados):
        response_text = dados.text
        return response_text
        
    @property
    def previsao_momento(self):
        return self.__previsao_momento

    @property
    def previsao_dia(self):
        return self.__previsao_dia
    
    @property
    def previsao_momento_bruto(self):
        return self.__previsao_momento_bruto
    
    @property
    def previsao_dia_bruto(self):
        return self.__previsao_dia_bruto


    

