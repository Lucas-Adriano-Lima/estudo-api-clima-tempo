class Atualiza:

    def atualiza_dia(self, dado_dia):
        with open('dados/previsao dia.csv', encoding='latin_1', mode='a') as arquivo:
            for interador in dado_dia['data']:
                dados = '{},{},{},{},{},{},{}\n'.format(interador['date_br'],
                        interador['humidity']['humidity'], interador['pressure']['pressure'],
                        interador['rain']['precipitation'], interador['wind']['velocity'],
                        interador['wind']['direction'],interador['temperature']['temperature'])
                arquivo.write(dados)

    def atualiza_bruto_dia(self, dado_dia_bruto):
        with open('dados/previsao dia bruto.csv', encoding='latin_1', mode='a') as arquivo:
            arquivo.write(dado_dia_bruto)
        
    def atualiza_momento(self, dado_momento):
        with open('dados/previsao momento.csv', encoding='latin_1', mode='a') as arquivo:
            dados = '{},{},{},{},{},{},{},{}\n'.format(dado_momento['data']['date'], dado_momento['data']['temperature'],
                    dado_momento['data']['wind_direction'], dado_momento['data']['wind_velocity'], dado_momento['data']['humidity'],
                    dado_momento['data']['condition'], dado_momento['data']['pressure'],dado_momento['data']['sensation'])
            arquivo.write(dados)
    
    def atualiza_momento_bruto(self, dado_momento_bruto):
        with open('dados/previsao momento bruto.csv', encoding='latin_1', mode='a') as arquivo:
            arquivo.write(dado_momento_bruto)
