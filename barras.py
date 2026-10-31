import pandas as pd
import matplotlib.pyplot as plt


def criar_grafico(df: pd.DataFrame):
    pivot = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
    ax = pivot.plot(kind="bar", figsize=(10, 6))
    ax.set_title("Vendas Médias por Categoria e Região")
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Vendas Médias")
    ax.tick_params(axis="x", labelrotation=45)
    ax.figure.tight_layout()
    return ax.figure


if __name__ == "__main__":
    df = pd.read_csv("dados_barras.csv")
    figura = criar_grafico(df)
    figura.savefig("01_barras.png", dpi=300)
    plt.show()
