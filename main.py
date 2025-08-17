import whisper
import os
import time

def diccionario_audios(ruta_carpeta: str) -> dict:
    if not os.path.exists(ruta_carpeta):
        print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
        return {}

    diccionario = {}
    for num, nombre_archivo in enumerate(os.listdir(ruta_carpeta), 1):
        if nombre_archivo.endswith((".mp3", ".m4a", ".wav", ".flac", ".aac", ".ogg", ".wma", ".alac")):
            ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
            try:
                tamaño_archivo = os.path.getsize(ruta_completa)
                diccionario[str(num)] = [nombre_archivo, tamaño_archivo]
            except OSError as e:
                print(f"Error al obtener el tamaño de '{nombre_archivo}': {e}")
    return diccionario

def getfiles(audios: str = 'audios') -> list:
    diccionario = diccionario_audios(audios)
    if not diccionario:
        print("No se encontraron archivos de audio en la carpeta especificada.")
        return []

    while True:
        try:
            print("\nArchivos disponibles:")
            for clave, valor in diccionario.items():
                print(f"{clave}) {valor[0]} - Tamaño: {valor[1] / (1024 * 1024):.2f} MB")

            opcion = input("\nSeleccione los números de los archivos separados por coma (ej: 1,3,5): ")
            seleccionados = opcion.replace(" ", "").split(",")

            archivos = []
            for num in seleccionados:
                if num in diccionario:
                    archivos.append(os.path.join(audios, diccionario[num][0]))
                else:
                    print(f"Opción '{num}' no válida. Ignorada.")

            if archivos:
                return archivos
            else:
                print("No se seleccionó ningún archivo válido. Intente nuevamente.")
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

    audio_files = getfiles()
    if not audio_files:
        return

    plural = '(s)' if len(audio_files) > 1 else ''
    print(f"\nTranscribiendo {len(audio_files)} archivo{plural} con el modelo {modelo_seleccionado}...\n")

    try:
        model = whisper.load_model(modelo_seleccionado)

        for audio_file in audio_files:
            if not os.path.isfile(audio_file):
                print(f"Error: El archivo '{audio_file}' no existe.")
                continue

            print(f"\nTranscribiendo: {os.path.basename(audio_file)}")

            start_time = time.time()
            result = model.transcribe(audio_file, verbose=False)
            end_time = time.time()

            transcription_time = end_time - start_time
            print(f"✔ Transcripción completada en {transcription_time:.2f} segundos.")

            output_filename = os.path.basename(audio_file).rsplit('.', 1)[0] + '.txt'
            output_filename = os.path.join("txt", output_filename)
            with open(output_filename, 'w', encoding="utf8") as f:
                f.writelines(result["text"])
            print(f"📝 Guardado en '{output_filename}'.")

    except Exception as e:
        print(f"Error durante la transcripción: {e}")

def generar_menu(opciones: dict):
    opcion = None
    while opcion != '7':
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)

def run():
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
