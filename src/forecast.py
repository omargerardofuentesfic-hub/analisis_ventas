import pandas as pd
from src.cargar_datos import cargar_datos


def ejecutar_forecast():
    print("\n🔮 PRONÓSTICO DE VENTAS\n")

    df = cargar_datos()

    # Ventas diarias
    ventas_diarias = df.groupby("fecha")["ventas"].sum().reset_index()

    # Promedio móvil simple
    ventas_diarias["promedio"] = ventas_diarias["ventas"].rolling(window=3).mean()

    # Proyección simple
    ultima_fecha = ventas_diarias["fecha"].max()
    ultimo_valor = ventas_diarias["promedio"].iloc[-1]

    fechas_futuras = pd.date_range(
        start=ultima_fecha + pd.Timedelta(days=1),
        periods=5
    )

    forecast = pd.DataFrame({
        "fecha": fechas_futuras,
        "ventas_estimadas": ultimo_valor
    })

    print("📅 Ventas futuras estimadas:")
    print(forecast)


if __name__ == "__main__":
    ejecutar_forecast()
