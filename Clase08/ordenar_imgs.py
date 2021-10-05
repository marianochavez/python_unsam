import os
from datetime import datetime


def procesar_nombre(fname):
    """Obtiene la fecha descripta en el fname y retorna
        esa fecha y su nombre nuevo sin la fecha"""
    file_name, file_ext = os.path.splitext(fname)
    date = file_name.split('_')[-1]
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    new_date = datetime(year=year, month=month, day=day)
    new_name = str.replace(fname, f'_{date}', '')
    return new_name, new_date


def procesar(directorio, new_dir_imgs="../Data/imgs_procesadas"):
    """Procesa los archivos .png de un directorio cambiando el access y modified
        time y nombre del archivo, utilizando la fn procesar_nombre, y lo mueve 
        a un nuevo directorio. Borra los directorios que quedaron vacios."""
    if not os.path.exists(new_dir_imgs):
        #  if path or directory doesn't exists
        os.mkdir(new_dir_imgs)

    for root, dirs, files in os.walk(directorio, topdown=False):
        for name in files:
            if name[-4:] == '.png':
                file = os.path.join(root, name)
                new_name, new_date = procesar_nombre(name)
                new_dir_name = os.path.join(new_dir_imgs, new_name)
                new_st_mod = new_date.timestamp()
                # change access and modified time
                os.utime(file, (new_st_mod, new_st_mod))
                # change directory and name file
                os.rename(file, new_dir_name)
            else:
                pass
        for name in dirs:
            # remove empty directory
            try:
                os.rmdir(os.path.join(root, name))
            except:
                pass


# if __name__ == "__main__":
    # import sys
#     try:
#         if len(sys.argv) == 3:
#             procesar(sys.argv[1],sys.argv[2])
#         else:
#             procesar(sys.argv[1])
#     except Exception as err:
#         print(f'Error: {err}')
