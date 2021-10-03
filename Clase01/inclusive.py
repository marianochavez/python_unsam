frase = 'todos somos programadores'
palabras = frase.split()
for palabra in palabras:
    pal_list = list(palabra)
    if pal_list[-1] == "o":
        pal_list[-1]="e"
    elif pal_list[-2] == "o":
        pal_list[-2]="e"
    print("".join(pal_list))