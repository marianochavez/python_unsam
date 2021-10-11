class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)


class Rectangulo():
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def __str__(self):
        return f'({self.punto_a}, {self.punto_b})'

    def __repr__(self) -> str:
        return f'Rectangulo({self.punto_a}, {self.punto_b})'

    def base(self):
        if self.punto_a.x < self.punto_b.x:
            return self.punto_b.x - self.punto_a.x
        return self.punto_a.x - self.punto_b.x

    def altura(self):
        if self.punto_a.y < self.punto_b.y:
            return self.punto_b.y - self.punto_a.y
        return self.punto_a.y - self.punto_b.y

    def area(self):
        return self.base()*self.altura()

    def desplazar(self, desplazamiento):
        self.punto_a = self.punto_a + desplazamiento
        self.punto_b = self.punto_b + desplazamiento
        return self.punto_a, self.punto_b

    def rotar(self):
        """Rotacion sobre el punto inferior derecho"""
        # encuentro el punto inf der
        if self.punto_a.x > self.punto_b.x:
            punto_rotacion = self.punto_a
        else:
            punto_rotacion = Punto(self.punto_b.x, self.punto_a.x)
        punto_extremo = Punto(punto_rotacion.x + self.altura(),
                              punto_rotacion.y + self.base())
        rect_rotado = Rectangulo(punto_rotacion,punto_extremo)
        return rect_rotado


ul = Punto(2, 2)
lr = Punto(5, 4)
ll = Punto(0, 0)
ur = Punto(1, 2)
rect1 = Rectangulo(ul, lr)
rect2 = Rectangulo(ll, ur)
desplazamiento = Punto(1, 1)
# print(rect1.desplazar(desplazamiento))
print(rect1.rotar())
