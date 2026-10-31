import pandas as pd
import matplotlib.pyplot as plt


def criar_grafico(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))
    for sexo, grupo in df.groupby("sexo"):
        ax.scatter(grupo["altura_cm"], grupo["peso_kg"], label=sexo, alpha=0.7)
    ax.set_title("Relação entre Altura e Peso")
    ax.set_xlabel("Altura (cm)")
    ax.set_ylabel("Peso (kg)")
    ax.legend()
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_dispersao.csv")
    figura = criar_grafico(df)
    figura.savefig("03_dispersao.png", dpi=300)
    plt.show()
