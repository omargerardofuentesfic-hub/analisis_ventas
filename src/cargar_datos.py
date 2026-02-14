import pandas as pd
from src.utils import ruta_datos

def cargar_datos():
    ruta = ruta_datos("ventas.csv")
    df = pd.read_csv(ruta)

    df["fecha"] = pd.to_datetime(df["fecha"])

    # Cálculos base
    df["ventas"] = df["unidades"] * df["precio_unitario"]
    df["costo_total"] = df["unidades"] * df["costo_unitario"]

    return df


if __name__ == "__main__":
    df = cargar_datos()
    print(df.head())
