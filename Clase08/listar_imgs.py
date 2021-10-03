import os


def archivos_png(directorio):
    """Imprime en consola los archivos .png encontrados
        en el directorio y subdirectorios"""
    png_files = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            file_name, file_ext = os.path.splitext(name)
            if file_ext == '.png':
                png_files.append(name)
    print(png_files)

if __name__ == '__main__':
    import sys
    archivos_png(sys.argv[1])
