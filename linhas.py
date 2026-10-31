import pandas as pd
import matplotlib.pyplot as plt


def criar_grafico(df: pd.DataFrame):
    dados = df.assign(data=pd.to_datetime(df["data"]))
    fig, ax = plt.subplots(figsize=(12, 6))
    for loja, grupo in dados.groupby("loja"):
        grupo = grupo.sort_values("data")
        ax.plot(grupo["data"], grupo["vendas"], label=loja)
    ax.set_title("Vendas ao Longo do Tempo por Loja")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    ax.legend()
    ax.tick_params(axis="x", labelrotation=45)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_linhas.csv")
    figura = criar_grafico(df)
    figura.savefig("07_linhas.png", dpi=300)
    plt.show()
