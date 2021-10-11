"""ERROR DE EJERCICIO:
    El error se encontraba en el parametro opcional contenido=[] ya que en la
    carga del programa, se calcula una vez, por lo tanto al modificar esa lista
    ya sea para el hijo o la madre, ambos usaban la misma lista. Se deben usar
    tipos inmutables.

    def __init__(self, nombre, contenido=[]):

        self.nombre = nombre
        self.contenido_marsupio = contenido
    """

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if contenido is None:
            contenido = []
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = ['Nobre canguro:' + self.nombre + '. Contenido del marsupio:']
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro)
# print(cangurito)