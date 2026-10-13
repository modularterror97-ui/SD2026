import time

def ciclo ():
    cnt = 0
    print("Iniciando ciclo infinito de saludos...")
    try:
        while True:
            print(f"{cnt}: Hola este es mi saludo: {cnt}")
            cnt += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ciclo interrumpido por el usuario.")

if __name__ == "__main__":
    ciclo()