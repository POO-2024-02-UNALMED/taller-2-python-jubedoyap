class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, nuevoColor):
        if nuevoColor == "rojo" or nuevoColor == "verde" or nuevoColor == "amarillo" or nuevoColor == "negro" or nuevoColor == "blanco":
            self.color = nuevoColor

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self, asientos):
        return asientos(len)
    
    def verificarIntegridad(self, motor, registro, asientos):
        mensaje = "Las piezas no son originales"
        if asientos(len) != 0:
            if (motor.registro == registro):
                j = 0
                for i in range(asientos(len)):
                    if registro == asientos[i].registro:
                        j += 1
                if j == asientos(len):
                    mensaje = "Auto original"
        return mensaje
      
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, tipoMotor):
        if tipoMotor == "electrico" or tipoMotor == "gasolina":
            self.tipo = tipoMotor

