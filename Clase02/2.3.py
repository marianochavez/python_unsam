f = open('../Data/precios.csv', 'rt')
for line in f:
    row = line.split(",")
    if row[0] == 'Naranja':
        precio_naranja = float(row[1])
print(f"El precio de la naranja es: {precio_naranja}")
f.close()