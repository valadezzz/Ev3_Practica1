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

    def set_peso(self, peso):
        if peso > 0:
            self.__peso = peso
        else:
            print("El peso no puede ser 0")

    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            print("La altura no puede ser 0")

    def set_sexo(self, sexo):
        self.__sexo = sexo


    def info(self):
        return f"""
        Nombre: {self.__nombre}
        Edad: {self.__edad}
        Peso: {self.__peso} kg
        Altura: {self.__altura} m
        Sexo: {self.__sexo}
        """

    def calcular_imc(self):
        return self.__peso / (self.__altura ** 2)
    
