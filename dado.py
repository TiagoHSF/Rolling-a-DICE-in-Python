# Simular o uso de um dado gerando um valor entre 1 e 6.

import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Roll the dice?'

    def Iniciar(self):
         resposta = input(self.mensagem)
        if resposta == 'sim' or resposta == 's':
            self.GerarValorDoDado()
        elif resposta == 'não' or resposta == 'n':
            print('Agradecemos pela participação!')
        else: 
            print('Favor digitar sim ou não')
    exception: 
        print('Ocorreu um erro ao processar sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()