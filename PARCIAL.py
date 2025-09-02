class Viaje:
    def __init__(self, ruta, tipo, costo, tiempo):
        self.ruta = ruta
        self.tipo = tipo  # 'urbana' o 'rural'
        self.costo = costo
        self.tiempo = tiempo  # en minutos

    def __str__(self):
        return f"Ruta: {self.ruta}, Tipo: {self.tipo}, Costo: ${self.costo:.2f}, Tiempo: {self.tiempo} min"

class RegistroViajes:
    def __init__(self):
        self.viajes = []

    def agregar_viaje(self, viaje):
        self.viajes.append(viaje)

    def mostrar_viajes(self):
        print("\n--- VIAJES REGISTRADOS ---")
        for i, viaje in enumerate(sorted(self.viajes, key=lambda v: v.ruta), 1):
            print(f"{i}. {viaje}")

    def resumen_semanal(self):
        total_costo = sum(v.costo for v in self.viajes)
        total_tiempo = sum(v.tiempo for v in self.viajes)
        print("\n--- RESUMEN SEMANAL ---")
        print(f"Gasto total: ${total_costo:.2f}")
        print(f"Tiempo total: {total_tiempo} minutos")

def main():
    registro = RegistroViajes()
    while True:
        print("\nIngrese los datos del viaje:")
        ruta = input("Ruta: ")
        tipo = input("Tipo (urbana/rural): ")
        try:
            costo = float(input("Costo ($): "))
            tiempo = int(input("Tiempo (minutos): "))
        except ValueError:
            print("Datos inválidos. Intente de nuevo.")
            continue

        viaje = Viaje(ruta, tipo, costo, tiempo)
        registro.agregar_viaje(viaje)

        otro = input("¿Desea ingresar otro viaje? (s/n): ").lower()
        if otro != 's':
            break

    registro.mostrar_viajes()
    registro.resumen_semanal()

if __name__ == "__main__":
    main()