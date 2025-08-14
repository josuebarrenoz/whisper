import whisper
import os
import time

def diccionario_audios(ruta_carpeta: str) -> dict:
    if not os.path.exists(ruta_carpeta):
        print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
        return {}

    diccionario = {}
    for num, nombre_archivo in enumerate(os.listdir(ruta_carpeta), 1):
        if nombre_archivo.endswith((".mp3", ".m4a", ".wav", ".flac", ".ogg")):
            ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
            try:
                tamaño_archivo = os.path.getsize(ruta_completa)
                diccionario[str(num)] = [nombre_archivo, tamaño_archivo]
            except OSError as e:
                print(f"Error al obtener el tamaño de '{nombre_archivo}': {e}")
    return diccionario

def getfile(audios: str = 'audios') -> str:
    diccionario = diccionario_audios(audios)
    if not diccionario:
        print("No se encontraron archivos de audio en la carpeta especificada.")
        return None

    while True:
        try:
            print("\nArchivos disponibles:")
            for clave, valor in diccionario.items():
                print(f"{clave}) {valor[0]} - Tamaño: {valor[1] / (1024 * 1024):.2f} MB")
            opcion = input("\nSeleccione el número del archivo que desea transcribir: ")
            if opcion in diccionario:
                return os.path.join(audios, diccionario[opcion][0])
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
        except Exception as e:
            print(f"Error: {e}. Intente nuevamente.")

def inicio():
    print("""
----------------------
|Bienvenido a Whisper|
----------------------
""")

def mostrar_menu(opciones: dict):
    print('\nSeleccione un modelo para la transcripción:')
    for clave in sorted(opciones, key=int):
        print(f' {clave}) {opciones[clave]}')

def leer_opcion(opciones: dict) -> str:
    while True:
        a = input("\nOpción: ")
        if a in opciones:
            return a
        print('Opción incorrecta, vuelva a intentarlo.')

def ejecutar_opcion(opcion: str, opciones: dict):
    modelo_seleccionado = opciones[opcion]
    if modelo_seleccionado == 'salir':
        return

    audio_file = getfile()
    if not audio_file:
        return

    if not os.path.isfile(audio_file):
        print(f"Error: El archivo '{audio_file}' no existe.")
        return

    print(f"\nTranscribiendo el archivo: {os.path.basename(audio_file)} con el modelo {modelo_seleccionado}...\n")

    try:
        model = whisper.load_model(modelo_seleccionado)

        start_time = time.time() # Iniciar el contador de tiempo
        result = model.transcribe(audio_file, verbose=False) # verbose=False para menos salida en consola
        end_time = time.time() # Finalizar el contador de tiempo

        transcription_time = end_time - start_time
        print(f"\n¡Transcripción completada en {transcription_time:.2f} segundos! 🎉")

        output_filename = os.path.basename(audio_file).rsplit('.', 1)[0] + '.txt'
        with open(output_filename, 'w', encoding="utf8") as f:
            f.writelines(result["text"])
        print(f"El texto transcribido se ha guardado en '{output_filename}'.")

    except Exception as e:
        print(f"Error durante la transcripción: {e}")

def generar_menu(opciones: dict):
    opcion = None
    while opcion != '7':
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)

def run():
    """Define las opciones del menú principal y ejecuta el programa."""
    opciones = {
        '1': 'tiny',
        '2': 'base',
        '3': 'small',
        '4': 'medium',
        '5': 'large',
        '6': 'turbo',
        '7': 'salir'
    }
    generar_menu(opciones)

if __name__ == "__main__":
    try:
        inicio()
        run()
        print("\nSaliendo del programa... ¡Hasta luego! 👋")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Saliendo... 👋")