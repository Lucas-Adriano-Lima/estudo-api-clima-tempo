from Previsao import Previsao
from Atualiza import Atualiza

if __name__ == '__main__' :
    previsao = Previsao()
    atualiza = Atualiza()
    dia = previsao.previsao_dia
    dia_bruto = previsao.previsao_dia_bruto
    momento = previsao.previsao_momento
    momento_bruto = previsao.previsao_momento_bruto
    atualiza.atualiza_dia(dia)
    atualiza.atualiza_bruto_dia(dia_bruto)
    atualiza.atualiza_momento(momento)
    atualiza.atualiza_momento_bruto(momento_bruto)
    print("Finalizado. Dados atualizados")
