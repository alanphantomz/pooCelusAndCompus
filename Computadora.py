class Computadora:
    tecnologia = "Computadores"

    def __init__(self):
        self.procesador = ""
        self.ram = 0
        self.hardDisk = 0

    def setProcesador(self, proc):
        self.procesador = proc

    def setRam(self, ram):
        self.ram = ram

    def setHardDisk(self, hd):
        self.hardDisk = hd

    def mostrarComputador(self):
        print("---COMPUTADOR---")
        print("Procesador: %s"%self.procesador)
        print("Ram: %d"%self.ram)
        print("Disco Duro: %d"%self.hardDisk)

    def leerDatos(self):
        print("Ingrese los datos solicitados a continuación")
        self.procesador = input("Procesador: ")
        self.ram = int(input("Ram: "))
        self.hardDisk = int(input("Disco Duro: "))