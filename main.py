import Computadora
import Celular
def main():

    #  Creando celular
    miCelular = Celular.Celular();

    #  Cargando propiedades al celular
    miCelular.setModelo("Y7 mini")
    miCelular.setMarca("Samsung")
    miCelular.setColor("Plateado")
    miCelular.setPulgadas(5.5)

    #  Mostrando celular
    miCelular.mostrarCelular()
    print("El valor estatico es: %s"%Celular.Celular.tecnologia)
    print("El valor estatico es: %s" % miCelular.tecnologia)

    #  Creando un computador
    miCompu = Computadora.Computadora();
    miCompu.setHardDisk(512)
    miCompu.setRam(6)
    miCompu.setProcesador("Core i3")

    miCompu.mostrarComputador()
    print("El valor estatico para compu es: %s"%Computadora.Computadora.tecnologia)
    print("El valor estatico para compu es: %s" % miCompu.tecnologia)

    #  Ahora vamos a crear un computador y un celular, y vamos a leer los datos de los mismos

    otroCelu = Celular.Celular()
    otroCelu.leerDatos()
    print("Tus datos ingresados fueron: ")
    otroCelu.mostrarCelular()

    otraCompu = Computadora.Computadora()
    otraCompu.leerDatos()
    print("Tus datos ingresados fueron: ")
    otraCompu.mostrarComputador()

if __name__ == '__main__':
    main()
