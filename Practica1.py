class Salud:
    def __init__ (self,nombre,edad,peso,altura,sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    