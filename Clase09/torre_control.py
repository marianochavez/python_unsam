class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl:
    '''Simula una torre de control de un aeropuerto, los aviones que estan
    esperando para aterrizar tienen prioridad sobre los que despegan.
    '''

    def __init__(self):
        '''Crea dos colas vacias'''
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, avion):
        '''Agrega un vuelo para aterrizar a cola'''
        self.arribos.encolar(avion)

    def nueva_partida(self, avion):
        '''Agrega un vuelo para despegar a cola'''
        self.partidas.encolar(avion)

    def ver_estado(self):
        '''Imprime los vuelos de arribos y partidas'''

        if not self.arribos.esta_vacia():
            vuelos = []
            for vuelo in self.arribos.items:
                vuelos.append(vuelo)
            print('Vuelos esperando para aterrizar:', ', '.join(vuelos))

        if not self.partidas.esta_vacia():
            vuelos = []
            for vuelo in self.partidas.items:
                vuelos.append(vuelo)
            print('Vuelos esperando para despegar:', ', '.join(vuelos))

    def asignar_pista(self):
        '''Elimina de la cola los aviones con prioridad de aterrizar y despues los 
        aviones que tienen que despegar'''

        if self.arribos.esta_vacia() and self.partidas.esta_vacia():
            print('No hay vuelos en espera.')
        elif self.arribos.esta_vacia():
            print(f'El vuelo {self.partidas.desencolar()} despegó con exito.')
        else:
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con exito.')


# torre = TorreDeControl()
# torre.nuevo_arribo('AR156')
# torre.nueva_partida('KLM1267')
# torre.nuevo_arribo('AR32')
# torre.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
