import math

class Circulo :
    # atributo
    radio = 0
    def __init__ (self, radio = 0) :
        self.radio = radio
    def area (self) :
        return round(math.pi * self.radio ** 2, 2)
    def perimetro (self) :
        return round(2 * math.pi * self.radio, 2)
# instanciar un circulo de radio 1
c1 = Circulo (1)
print (c1.area())        # 3.14
print (c1.perimetro())   # 6.28
# instanciar un circulo, y luego agregar el radio
c2 = Circulo ()
c2.radio = 2
print (c2.area())        # 12.57
print (c2.perimetro())   # 12.57

