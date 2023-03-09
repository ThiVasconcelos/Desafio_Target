import json

class Faturamento:

    def __init__(self, file_path):
        with open(file_path , 'r') as file:
            self.data = json.load(file)
        self.menor_faturamento = float('inf')
        self.maior_faturamento = 0
        self.media_faturamento = 0
        self.dias_acima_da_media = 0
        self.calcular_faturamento()

    def calcular_faturamento(self):
        soma_total_faturamento = 0
        dias_com_faturamento = 0
        for dia in self.data:
            if dia['valor'] > 0:
                soma_total_faturamento += dia['valor']
                dias_com_faturamento += 1
                if dia['valor'] < self.menor_faturamento:
                    self.menor_faturamento = dia['valor']
                if dia['valor'] > self.maior_faturamento:
                    self.maior_faturamento = dia['valor']
        self.media_faturamento = soma_total_faturamento / dias_com_faturamento
        self.dias_acima_da_media = len([dia for dia in self.data if dia['valor'] > self.media_faturamento])

    def mostrar_calculos(self):
        print('Menor faturamento: R$', self.menor_faturamento)
        print('Maior faturamento: R$', self.maior_faturamento)
        print('Número de dias com faturamento acima da média mensal:', self.dias_acima_da_media)


faturamento = Faturamento('scr\data\dados1.json')
faturamento.mostrar_calculos()


