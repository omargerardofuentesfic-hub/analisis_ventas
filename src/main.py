import sys
import os
from src import kpis,analisis_tendencias,graficas,forecast

# 🔧 Asegurar que src esté en el path (clave para PyInstaller)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

if base_path not in sys.path:
    sys.path.insert(0, base_path)




def mostrar_menu():
    print("\n==============================")
    print(" SISTEMA DE ANÁLISIS DE VENTAS ")
    print("==============================")
    print("1. Ver KPI's del negocio")
    print("2. Generar gráficas")
    print("3. Análisis de tendencias")
    print("4. Pronóstico de ventas")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            kpis.ejecutar_kpis()

        elif opcion == "2":
            graficas.ejecutar_graficas()

        elif opcion == "3":
            analisis_tendencias.ejecutar_analisis()

        elif opcion == "4":
            forecast.ejecutar_forecast()

        elif opcion == "0":
            print("\n👋 Saliendo del sistema. ¡Hasta luego!")
            if getattr(sys, 'frozen', False):
                input("\nPresiona ENTER para cerrar...")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
