cadena = "Geringoso"
capadepenapa = ''

for c in cadena:
    capadepenapa += c
    if c == "a":
        capadepenapa += "pa"
    elif c == "e":
        capadepenapa += "pe"
    elif c == "i":
        capadepenapa += "pi"
    elif c == "o":
        capadepenapa += "po"
    elif c == "u":
        capadepenapa += "pu"

print(capadepenapa)
