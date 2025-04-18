from collections import deque

class Tarea:
    def __init__(self, id, duracion, prioridad):
        if duracion <= 0 or prioridad < 0:
            raise ValueError("Duración debe ser > 0 y prioridad >= 0")
        self.id = id
        self.duracion = duracion
        self.prioridad = prioridad
        self.restante = duracion
        self.inicio = None
        self.fin = None

class PlanificadorRoundRobin:
    def __init__(self, quantum):
        if quantum <= 0:
            raise ValueError("El quantum debe ser mayor que 0")
        self.cola = deque()
        self.quantum = quantum
        self.tiempo = 0
        self.historial = []

    def agregar_tarea(self, tarea):
        self.cola.append(tarea)

    def ejecutar(self):
        while self.cola:
            tarea = self.cola.popleft()

            if tarea.inicio is None:
                tarea.inicio = self.tiempo

            tiempo_ejecucion = min(self.quantum, tarea.restante)
            self.tiempo += tiempo_ejecucion
            tarea.restante -= tiempo_ejecucion

            if tarea.restante > 0:
                self.cola.append(tarea)
            else:
                tarea.fin = self.tiempo
                self.historial.append(tarea)

    def mostrar_resultados(self):
        total_espera = 0
        total_respuesta = 0

        print("\nResultados de ejecución:")
        for t in self.historial:
            espera = (t.fin - t.duracion)
            respuesta = t.inicio
            total_espera += espera
            total_respuesta += respuesta
            print(f"Tarea-{t.id}: Espera = {espera}, Respuesta = {respuesta}, Finaliza en = {t.fin}")

        n = len(self.historial)
        print(f"\nTiempo total: {self.tiempo}")
        print(f"Tiempo promedio de espera: {total_espera / n:.2f}")
        print(f"Tiempo promedio de respuesta: {total_respuesta / n:.2f}")

# Casos de prueba
def prueba_1():
    planificador = PlanificadorRoundRobin(quantum=4)
    planificador.agregar_tarea(Tarea(1, duracion=10, prioridad=1))
    planificador.agregar_tarea(Tarea(2, duracion=5, prioridad=2))
    planificador.agregar_tarea(Tarea(3, duracion=8, prioridad=1))

    planificador.ejecutar()
    planificador.mostrar_resultados()

def prueba_2():
    planificador = PlanificadorRoundRobin(quantum=3)
    planificador.agregar_tarea(Tarea(1, duracion=15, prioridad=1))
    planificador.agregar_tarea(Tarea(2, duracion=8, prioridad=2))
    planificador.agregar_tarea(Tarea(3, duracion=5, prioridad=3))
    planificador.agregar_tarea(Tarea(4, duracion=6, prioridad=2))
    planificador.agregar_tarea(Tarea(5, duracion=7, prioridad=1))

    planificador.ejecutar()
    planificador.mostrar_resultados()

# Función principal para ejecutar ambos ejemplos
if __name__ == "__main__":
    print("Ejemplo 1:")
    prueba_1()

    print("\nEjemplo 2:")
    prueba_2()
