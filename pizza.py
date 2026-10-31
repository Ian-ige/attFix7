import pandas as pd
import matplotlib.pyplot as plt


def criar_grafico(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        df["faturamento"],
        labels=df["canal_venda"],
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title("Faturamento por Canal de Venda")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_pizza.csv")
    figura = criar_grafico(df)
    figura.savefig("08_pizza.png", dpi=300)
    plt.show()
