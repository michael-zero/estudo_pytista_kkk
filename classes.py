class Veiculo:
   movimenta = True 

   def __init__(self, num_rodas, tipo, ano):
       self.rodas = num_rodas
       self.tipo = tipo
       self.ano = ano

   def info(self):
       print(f'vehicle is of type {self.tipo}')
  
   def calcular(self):
       pass

   @classmethod 
   def mover(cls):
       print(f'movimenta = {cls.movimenta}')
    
   @staticmethod
   def colorir():
       print(f'All cars will be blue')

class construcao:
    pass


carro = Veiculo(4,'carro',98)
carro.info()
carro.colorir()


casa = construcao()

Veiculo.mover()
Veiculo.colorir()

