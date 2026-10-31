import pandas as pd
import matplotlib.pyplot as plt


def criar_grafico(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df["idade"], bins=10, edgecolor="black")
    ax.set_title("Distribuição das Idades dos Clientes")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Frequência")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_distribuicao.csv")
    figura = criar_grafico(df)
    figura.savefig("04_distribuicao.png", dpi=300)
    plt.show()
