import matplotlib.pyplot as plt
from src.cargar_datos import cargar_datos
from src.utils import ruta_datos
import os

def ejecutar_graficas():
    print("\n📊 Generando gráficas...\n")

    df = cargar_datos()

    # Crear carpeta de salida
    carpeta = ruta_datos("graficas")
    os.makedirs(carpeta, exist_ok=True)

    # 📈 Ventas por fecha
    ventas_fecha = df.groupby("fecha")["ventas"].sum()
    plt.figure()
    ventas_fecha.plot(title="Ventas por día")
    plt.xlabel("Fecha")
    plt.ylabel("Ventas")
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, "ventas_diarias.png"))
    plt.close()

    # 📦 Ventas por producto
    ventas_producto = df.groupby("producto")["ventas"].sum()
    plt.figure()
    ventas_producto.plot(kind="bar", title="Ventas por producto")
    plt.xlabel("Producto")
    plt.ylabel("Ventas")
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, "ventas_producto.png"))
    plt.close()

    # 👤 Ventas por cliente
    ventas_cliente = df.groupby("cliente")["ventas"].sum()
    plt.figure()
    ventas_cliente.plot(kind="bar", title="Ventas por cliente")
    plt.xlabel("Cliente")
    plt.ylabel("Ventas")
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, "ventas_cliente.png"))
    plt.close()

    print("✅ Gráficas generadas correctamente")
