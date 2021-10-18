class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any(lote for lote in self.lotes if lote.nombre == nombre)

    def __len__(self):
        return len(self.lotes)

    def __getitem__(self,n):
        return self.lotes[n]

    def __repr__(self):
        return f'Camion({self.lotes})'

    def __str__(self):
        text = [f'Camion con {len(self.lotes)}']
        for lote in self.lotes:
            text.append(f'Lote de {lote.cajones} cajones de {lote.nombre}, pagados a ${lote.precio} cada uno.')
        return '\n'.join(text)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total

