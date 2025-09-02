import re
from collections import defaultdict

class Viaje:
    def __init__(self, num_ruta, origen, destino, tipo, costo, tiempo_minutos, pasajeros, dia):
        self.num_ruta = num_ruta
        self.origen = origen
        self.destino = destino
        self.tipo = tipo  # 'urbana' o 'rural'
        self.costo = costo
        self.tiempo = tiempo_minutos  # en minutos
        self.pasajeros = pasajeros
        self.dia = dia

    def ganancia(self):
        return self.costo * self.pasajeros

    def __str__(self):
        horas = self.tiempo // 60
        minutos = self.tiempo % 60
        tiempo_str = f"{horas} h {minutos} m" if horas else f"{minutos} m"
        return (f"Ruta #{self.num_ruta} | Origen: {self.origen} | Destino: {self.destino} | Ciudad: {self.destino} | "
                f"Tipo: {self.tipo} | Día: {self.dia} | Costo: ${self.costo:.2f} | Pasajeros: {self.pasajeros} | "
                f"Ganancia: ${self.ganancia():.2f} | Tiempo: {tiempo_str}")

class RegistroViajes:
    def __init__(self):
        self.viajes = []

    def agregar_viaje(self, viaje):
        self.viajes.append(viaje)

    def mostrar_viajes(self):
        print("\n--- VIAJES REGISTRADOS ---")
        for i, viaje in enumerate(self.viajes, 1):
            print(f"{i}. {viaje}")

    def resumen_por_dia(self):
        print("\n--- RESUMEN POR DÍA ---")
        ganancias_por_dia = defaultdict(float)
        pasajeros_por_dia = defaultdict(int)
        viajes_por_dia = defaultdict(int)
        for viaje in self.viajes:
            ganancias_por_dia[viaje.dia] += viaje.ganancia()
            pasajeros_por_dia[viaje.dia] += viaje.pasajeros
            viajes_por_dia[viaje.dia] += 1
        for dia in sorted(ganancias_por_dia):
            print(f"Día: {dia} | Total de viajes: {viajes_por_dia[dia]} | Pasajeros: {pasajeros_por_dia[dia]} | Ganancia total: ${ganancias_por_dia[dia]:.2f}")

    def resumen_semanal(self):
        total_ganancia = sum(v.ganancia() for v in self.viajes)
        total_pasajeros = sum(v.pasajeros for v in self.viajes)
        print("\n--- RESUMEN SEMANAL ---")
        print(f"Total de viajes: {len(self.viajes)}")
        print(f"Total de pasajeros: {total_pasajeros}")
        print(f"Total de ganancias en la semana: ${total_ganancia:.2f}")

def leer_tiempo():
    tiempo_str = input("Tiempo: ").lower().replace(" ", "")
    minutos = 0
    patron = r"(?:(\d+)h)?(?:(\d+)m)?"
    match = re.match(patron, tiempo_str)
    if match:
        h = match.group(1)
        m = match.group(2)
        if h:
            minutos += int(h) * 60
        if m:
            minutos += int(m)
        if minutos == 0:
            raise ValueError("Formato de tiempo inválido.")
    else:
        raise ValueError("Formato de tiempo inválido.")
    return minutos

def main():
    registro = RegistroViajes()
    while True:
        print("\nIngrese los datos del viaje:")
        num_ruta = input("Número de ruta: ")
        origen = input("Origen: ")
        destino = input("Destino: ")
        tipo = input("Tipo (urbana/rural): ")
        dia = input("Día: ")
        try:
            costo = float(input("Costo ($): "))
            pasajeros = int(input("Cantidad de pasajeros: "))
            tiempo = leer_tiempo()
        except ValueError:
            print("Datos inválidos. Intente de nuevo.")
            continue

        viaje = Viaje(num_ruta, origen, destino, tipo, costo, tiempo, pasajeros, dia)
        registro.agregar_viaje(viaje)

        otro = input("¿Desea ingresar otro viaje? (s/n): ").lower()
        if otro != 's':
            break

    registro.mostrar_viajes()
    registro.resumen_por_dia()
    registro.resumen_semanal()

if __name__ == "__main__":
    main()