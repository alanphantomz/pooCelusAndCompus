class Celular:
    """Una clase que abstrae a un celular de la vida real"""
    tecnologia = "celular" # variable de clase

    def __init__(self):
        '''Constructor de la clase'''
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.pulgadas = 0.0

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setColor(self, color):
        self.color = color

    def setPulgadas(self, plg):
        self.pulgadas = plg

    def mostrarCelular(self):
        print("---Objeto celular---")
        print("Marca: %s"%self.marca)
        print("Modelo: %s"%self.modelo)
        print("Color: %s"%self.color)
        print("Pulgadas: %.1f"%self.pulgadas)

    def leerDatos(self):
        print("Ingrese los datos solicitados a continuaación: ")
        self.marca = input("marca: ")
        self.modelo = input("modelo: ")
        self.color = input("color: ")
        self.pulgadas = float(input("pulgadas: "))