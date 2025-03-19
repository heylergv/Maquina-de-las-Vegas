import random  # importar libreria para seleccion de random
import time  # importar liberira para que tome tiempo en cargar las frutas y que parezca una maquina real

print("\n🎰🔥👑💲 Bienvenido a la Máquina de las Vegas 💲👑🔥🎰")


def maquina(): #Funcion principal (Esto es lo que hara el programa)
    frutas = ["🥭", "🍉", "🍎", "🍌"] #arreglo/lista de frutas para el juego

    while True:  # Mientras sea verdad o mientras el jugador quiera se ejecutara todo nuevamente
        pago = input("Ingresa un 💵 para girar (Copia y pega): ").strip()
        if pago != "💵":  # distinto de" o "no igual a" para este caso True: Si el usuario ingresó algo diferente al emoji 💵. y False: Si el usuario ingresó exactamente el emoji 💵.
            print("Por favor, ingresa el emoji 💵 para girar.")
            continue  # le dice al programa que vuelva al inicio del bucle sin ejecutar las líneas siguientes.

        resultado = []

        for _ in range(3): #En el rango de unicamente 3 valores...
            rueda = random.choice(frutas) #Se gira la rueda con una eleccion random que elige la libreria de la lista 'Frutas' (llamara solo 3 debido al for _ in range (3)
            resultado.append(rueda) #Ingresa en el arreglo resultado = [] aleatoriamente un elemento de la lista frutas de la la variable rueda
            print(f"{rueda}", end="", flush=True) #imprime seleccion de variable rueda, end="" evita que haga un salto de linea y flush=True para que se imprima inmediatamente sin esperar que el bucle termine simulando la maquina
            time.sleep(1) #Esta linea unicamente sirve para esperar a imprimir un elemente 1 segundo simulando la maquina, si la quitas imprime 3 elementos inmediatamente

        print()

        if resultado[0] == resultado[1] == resultado[2]: #Si las tres frutas son iguales entonces mostrara el mensaje felicidades
            print("🎉💸🤑💰💸🎉¡Felicidades!🎉💸💰🤑💸🎉")
            probabilidad = random.randint(1, 100)  # Genera un número entre 1 y 100
            if probabilidad <= 10:  # 10% de probabilidad para $1000
                premio = 1000
            else:  # 90% de probabilidad para otros premios en el array de premios
                premio = random.choice([100, 200, 500]) #Lista de premios adicionales
            print(f"💰¡Ganaste un premio de ${premio}!💰")

        else: #Si las 3 frutas no son iguales entonces mostrara el mensaje de seguir intentando
            print("🐸 ¡Sigue intentando! 🐸")


maquina() #Llamada para la funcion (Ahora ejecutara lo que hace la funcion)