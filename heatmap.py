import pandas as pd
import matplotlib.pyplot as plt


ORDEM_DIAS = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]


def criar_grafico(df: pd.DataFrame):
    tabela = df.pivot(
        index="dia_semana", columns="horario", values="movimento_clientes"
    )
    tabela = tabela.reindex([dia for dia in ORDEM_DIAS if dia in tabela.index])
    fig, ax = plt.subplots(figsize=(10, 6))
    imagem = ax.imshow(tabela.values, aspect="auto")
    fig.colorbar(imagem, ax=ax, label="Movimento de Clientes")
    ax.set_xticks(range(len(tabela.columns)), tabela.columns)
    ax.set_yticks(range(len(tabela.index)), tabela.index)
    ax.set_title("Movimento de Clientes por Dia e Horário")
    ax.set_xlabel("Horário")
    ax.set_ylabel("Dia da Semana")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.read_csv("dados_heatmap.csv")
    figura = criar_grafico(df)
    figura.savefig("06_heatmap.png", dpi=300)
    plt.show()
