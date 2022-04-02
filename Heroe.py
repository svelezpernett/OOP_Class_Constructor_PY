class Heroe:

    #CONSTRUCTOR(Funcion especial que permite inicializar los atributos)
    def __init__(self,name,height, poder):
        #atributosself
        self.poder=poder
        self.estatura=height
        self.nombre=name
        self.tipoHeroe=None
        self.cantidadVida=None
    

    


    #metodos
    def saludar(self):
        print("Hola")


#CREANDO UN OBJETO - utilizando la clase(Crear una instancia, sacarle fotocopia)
#Un objeto es una VARIABLE especial
batman = Heroe('Bruce Wayne', 1.90, 500)
joker = Heroe('nn', 1.70, 1200)

#con el objeto, accedo a un atributo
print(batman.nombre)
print(joker.poder)


#con el objeto taambien puedo acceder a un metodo
batman.saludar()
