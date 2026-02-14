from src.cargar_datos import cargar_datos

def ejecutar_kpis():
    print("\n📊 KPIs DE VENTAS\n")

    df = cargar_datos()

    ventas_totales = df["ventas"].sum()
    unidades_totales = df["unidades"].sum()
    ticket_promedio = ventas_totales / unidades_totales if unidades_totales > 0 else 0
    margen = ((df["precio_unitario"] - df["costo_unitario"]) * df["unidades"]).sum()

    print(f"💰 Ventas totales: ${ventas_totales:,.2f}")
    print(f"📦 Unidades vendidas: {unidades_totales}")
    print(f"🧾 Ticket promedio: ${ticket_promedio:,.2f}")
    print(f"📈 Margen total: ${margen:,.2f}")
