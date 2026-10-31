import pandas as pd
import matplotlib.pyplot as plt


def criar_grafico(df: pd.DataFrame):
    frequencia = df["tipo_atendimento"].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    frequencia.plot(kind="bar", ax=ax)
    ax.set_title("Frequência por Tipo de Atendimento")
    ax.set_xlabel("Tipo de Atendimento")
    ax.set_ylabel("Quantidade de Chamados")
    ax.tick_params(axis="x", labelrotation=45)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_frequencia.csv")
    figura = criar_grafico(df)
    figura.savefig("05_frequencia.png", dpi=300)
    plt.show()
