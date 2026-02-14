from src.cargar_datos import cargar_datos


def ejecutar_analisis():
    print("\n📈 ANÁLISIS DE TENDENCIAS\n")

    df = cargar_datos()

    # Ventas por fecha
    print("📅 Ventas por fecha:")
    ventas_fecha = df.groupby("fecha")["ventas"].sum()
    print(ventas_fecha)

    # Ventas por categoría
    print("\n📦 Ventas por categoría:")
    ventas_categoria = df.groupby("categoria")["ventas"].sum()
    print(ventas_categoria)

    # Productos más vendidos
    print("\n🏆 Productos más vendidos:")
    productos = df.groupby("producto")["unidades"].sum().sort_values(ascending=False)
    print(productos)


if __name__ == "__main__":
    ejecutar_analisis()
