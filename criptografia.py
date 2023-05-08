import random

caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'É', 'Í', 'Ó', 'Ú', '1',
              '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '^', '%', '#', '$', '@', ' ', ',', ';',
              '.', ':', '¿', '?', '¡', '!', '(', ')', '[', ']', '{', '}', '\\', '=', '¬', 'ñ', 'Ñ', 'ü', 'Ü']

a = random.randint(1, 100000000000000)
b = random.randint(1, 100000000000000)


def encriptar_mensaje(mensaje, a, b):
    global mensaje_hex
    mensaje_encriptado = ""
    for caracter in mensaje:
        indice = caracteres.index(caracter)
        indice_encriptado = (a * indice + b) % 104
        caracter_encriptado = caracteres[indice_encriptado]
        mensaje_encriptado += caracter_encriptado
        mensaje_hex = mensaje_encriptado.encode("utf-8").hex()

    forma = random.randint(1, 6)
    if forma == 1:
        mensaje_final = f"{a}&{b}&{mensaje_hex}"
    elif forma == 2:
        mensaje_final = f"{a}&{mensaje_hex}&{b}"
    elif forma == 3:
        mensaje_final = f"{b}&{a}&{mensaje_hex}"
    elif forma == 4:
        mensaje_final = f"{b}&{mensaje_hex}&{a}"
    elif forma == 5:
        mensaje_final = f"{mensaje_hex}&{a}&{b}"
    else:
        mensaje_final = f"{mensaje_hex}&{b}&{a}"

    return mensaje_final


def desencriptar_mensaje(mensaje_hex, a, b):
    # Convertir el mensaje hexadecimal a texto
    mensaje = bytes.fromhex(mensaje_hex).decode("utf-8")

    # Desencriptar el mensaje
    mensaje_desencriptado = ""
    for caracter in mensaje:
        indice = caracteres.index(caracter)
        inverso_a = pow(a, -1, 104)
        indice_desencriptado = inverso_a * (indice - b) % 104
        caracter_desencriptado = caracteres[indice_desencriptado]
        mensaje_desencriptado += caracter_desencriptado

    return mensaje_desencriptado


while True:
    print("Bienvenido a la maquina enigma")
    opcion = input("¿Qué desea hacer? (1) Encriptar mensaje, (2) Desencriptar mensaje, (3) Salir: ")

    if opcion == "1":
        mensaje = input("Ingrese el mensaje a encriptar: ")
        mensaje_final = encriptar_mensaje(mensaje, a, b)
        print(f"Mensaje encriptado: {mensaje_final}")
        print(f"numero random a: {a}")
        print(f"numero random b: {b}")

    elif opcion == "2":
        mensaje_encriptado = input("Ingrese el mensaje encriptado: ")
        a = int(input("Ingrese el numero random a: "))
        b = int(input("Ingrese el numero random b: "))
        mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, a, b)
        print(f"Mensaje desencriptado: {mensaje_desencriptado}")

    elif opcion == "3":
        print("Hasta la proxima")
        break

    else:
        print("Opción inválida. Vuelvalo a intentar.")
