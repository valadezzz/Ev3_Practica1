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

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def get_sexo(self):
        return self.__sexo
    


    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad


    
    def set_sexo(self, sexo):
        self.__sexo = sexo