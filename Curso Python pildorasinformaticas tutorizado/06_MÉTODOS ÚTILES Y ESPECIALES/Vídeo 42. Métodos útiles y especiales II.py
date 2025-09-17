class Persona():
    def __init__(self, name, s_name, age):
        self.nombre = name
        self.apellido = s_name
        self.edad = age

    def __str__(self):
        return f"Datos de la persona: \nNombre: {self.nombre} \nApellido: {self.apellido} \nEdad: {self.edad}"

persona01 = Persona("Jim", "Carrey", 18)
print(persona01)

class Person():

    almacen_datos=[]
    def __init__(self, **datos):
        for dato in datos:
            self.almacen_datos.append(dato)

        self.getDatos(self.almacen_datos)


persona02 = Person("willy","jimmy",32,58,23000)
persona02.getDatos()
print(persona02)