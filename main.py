import whisper
import os

def inicio():
    print("""
    ----------------------
    |Bienvenido a Whisper|
    ----------------------

    """)

def mostrar_menu(opciones:dict):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave]}')

def leer_opcion(opciones:dict,a:str=''):
    a = input("\nOpcion: ")
    while a not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion:str, opciones:dict):
    base = opciones[opcion]
    if base == 'salir':
        print("Saliendo del programa...")
        return
    audio_file = "TRINIDAD.mp3"
    if not os.path.isfile(audio_file):
        print(f"Error: El archivo '{audio_file}' no existe en la carpeta actual.")
        return
    model = whisper.load_model(base)
    result = model.transcribe(audio_file)
    with open(r'Resultados.txt', 'w', encoding="utf8") as f:
        f.writelines(result["text"])
    print("\nLa tarea se realizo exitosamente\n")


def generar_menu(opciones:dict, opcion_salida:str):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

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
    generar_menu(opciones, '7')


if __name__ == "__main__":
    try:
        inicio()
        run()
        print('\nSaliendo...')
    except KeyboardInterrupt:
        print('\nSaliendo...')


