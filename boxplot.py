import pandas as pd
import matplotlib.pyplot as plt


def criar_grafico(df: pd.DataFrame):
    grupos = list(df.groupby("departamento"))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(
        [grupo["salario"].values for _, grupo in grupos],
        tick_labels=[nome for nome, _ in grupos],
    )
    ax.set_title("Distribuição dos Salários por Departamento")
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Salário")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_boxplot.csv")
    figura = criar_grafico(df)
    figura.savefig("02_boxplot.png", dpi=300)
    plt.show()
