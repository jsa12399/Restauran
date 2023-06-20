import os
import time
import numpy
import funcione_jsa_ejemplo as fn



while True:
    print("""Menú
    1. Ver Restaurant
    2. Reservar Mesa
    3. Carta
    4. Pagar
    5. Cancelar
    6. Salir      """)
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.ver_restaurant()
    elif opcion == 2:
        fn.reservar_mesa()
    elif opcion ==3:
        fn.carta()
    elif opcion ==4:
        fn.pagar()
    else:
        break            


