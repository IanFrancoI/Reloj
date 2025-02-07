import time

while True:
    tiempo = time.strftime('%H:%M:%S')
    print(f'\rTiempo Actual: {tiempo}', end='')

    time.sleep(1)