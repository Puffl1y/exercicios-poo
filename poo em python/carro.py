class Motor:   
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def Ligar(self):
        return "Motor ligado!"

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
    
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}")
        print(f"Motorização: {self.motor.tipo} ({self.motor.potencia} cv)")
        print(f"Status: {self.motor.Ligar()}")