import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def criar_grafico(df: pd.DataFrame):
    x = df["renda_mensal"]
    y = df["gasto_mensal"]
    coeficientes = np.polyfit(x, y, 1)
    reta = np.poly1d(coeficientes)
    x_linha = np.linspace(x.min(), x.max(), 100)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, label="Dados")
    ax.plot(x_linha, reta(x_linha), label="Regressão Linear")
    ax.set_title("Regressão Linear entre Renda e Gasto Mensal")
    ax.set_xlabel("Renda Mensal")
    ax.set_ylabel("Gasto Mensal")
    ax.legend()
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_regressao.csv")
    figura = criar_grafico(df)
    figura.savefig("09_regressao.png", dpi=300)
    plt.show()
