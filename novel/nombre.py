import os

# Ruta de la carpeta donde están los archivos PDF
ruta_carpeta = 'D:\\personal\\Desktop\\proyecto\\novel'

# Recorrer los archivos desde capitulo_346 hasta capitulo_443
for i in range(1, 269):
    # Nombre actual del archivo
    nombre_actual = f'capitulo_{i}_traducido.pdf'
    # Nuevo nombre del archivo
    nuevo_nombre = f'capitulo_{i}.pdf'
    
    # Ruta completa del archivo actual y nuevo
    ruta_actual = os.path.join(ruta_carpeta, nombre_actual)
    ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)
    
    # Renombrar el archivo
    if os.path.exists(ruta_actual):
        os.rename(ruta_actual, ruta_nueva)
        print(f'Renombrado: {nombre_actual} -> {nuevo_nombre}')
    else:
        print(f'El archivo {nombre_actual} no existe.')