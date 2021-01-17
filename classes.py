from montadora.veiculo import Veiculo

carro = Veiculo(4,'carro',98)
carro.info()
carro.colorir()

Veiculo.mover()
Veiculo.colorir() #classmethod

print(carro.rodas)