from .cargar_datos import cargar_ventas, preparar_datos


def generar_reportes():
    df = cargar_ventas()
    df = preparar_datos(df)

    # Reporte diario
    reporte_diario = df.groupby("fecha")[["ventas", "costos"]].sum()
    reporte_diario["utilidad"] = reporte_diario["ventas"] - reporte_diario["costos"]

    # Reporte mensual
    reporte_mensual = df.groupby(df["fecha"].dt.to_period("M"))[["ventas", "costos"]].sum()
    reporte_mensual["utilidad"] = reporte_mensual["ventas"] - reporte_mensual["costos"]

    print("\n📅 REPORTE DIARIO")
    print(reporte_diario)

    print("\n📆 REPORTE MENSUAL")
    print(reporte_mensual)
