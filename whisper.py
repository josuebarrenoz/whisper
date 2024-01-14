import whisper

def inicio():
    print("""
    ----------------------
    |Bienvenido a Whisper|
    ----------------------

    """)


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('tiny', accion1),
        '2': ('base', accion2),
        '3': ('small', accion3),
        '4': ('medium', accion4),
        '5': ('large', accion5),
    }

    generar_menu(opciones, '5')


def accion1():
    base = str("tiny")


def accion2():
    base = str("base")


def accion3():
    base = str("small")

def accion4():
    base = str("medium")

def accion5():
    base = str("large")


def run():
    base =str()
    #archivo = str(input("Escribe el nombre del archivo con su extension: "));
    #ruta = f"C:\Users\Zapat\Repositorios\whisper{archivo}"
    menu_principal()
    model = whisper.load_model(base)
    #result = model.transcribe(ruta)
    result = model.transcribe("C:\Users\Zapat\Repositorios\whisper\TRINIDAD.mp3")
    with open(r'Resultados.txt', 'w', encoding="utf8") as f:
        f.writelines(result["text"])
    print("La tarea se realizo exitosamente")


if __name__ == "__main__":
    inicio()
    run()


