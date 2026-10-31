from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from barras import criar_grafico as criar_grafico_barras
from boxplot import criar_grafico as criar_grafico_boxplot
from dispersao import criar_grafico as criar_grafico_dispersao
from distribuicao import criar_grafico as criar_grafico_distribuicao
from frequencia import criar_grafico as criar_grafico_frequencia
from heatmap import criar_grafico as criar_grafico_heatmap
from linhas import criar_grafico as criar_grafico_linhas
from pizza import criar_grafico as criar_grafico_pizza
from regressao import criar_grafico as criar_grafico_regressao


PASTA_PROJETO = Path(__file__).resolve().parent


st.set_page_config(
    page_title="Painel de visualizações",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def carregar_dados(nome_arquivo: str) -> pd.DataFrame:
    caminho = PASTA_PROJETO / nome_arquivo
    if not caminho.is_file():
        raise FileNotFoundError(f"Arquivo de dados não encontrado: {caminho.name}")
    return pd.read_csv(caminho)


def formatar_valor(valor: float) -> str:
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def analisar_barras(df: pd.DataFrame) -> str:
    tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
    regiao = tabela.mean().idxmax()
    categoria = tabela[regiao].idxmax()
    valor = tabela.loc[categoria, regiao]
    return (
        f"A região **{regiao}** tem a maior média entre as regiões. "
        f"Nela, **{categoria}** lidera, com {formatar_valor(valor)}."
    )


def analisar_boxplot(df: pd.DataFrame) -> str:
    medianas = df.groupby("departamento")["salario"].median()
    departamento = medianas.idxmax()
    return (
        f"**{departamento}** apresenta a maior mediana salarial "
        f"({formatar_valor(medianas[departamento])}). "
        "A caixa mostra a faixa central dos salários de cada departamento."
    )


def analisar_dispersao(df: pd.DataFrame) -> str:
    correlacao = df["altura_cm"].corr(df["peso_kg"])
    direcao = "positiva" if correlacao >= 0 else "negativa"
    intensidade = "forte" if abs(correlacao) >= 0.7 else "moderada" if abs(correlacao) >= 0.4 else "fraca"
    return (
        f"Há uma associação **{direcao} {intensidade}** entre altura e peso "
        f"(correlação de {correlacao:.2f}); isso não implica causalidade."
    )


def analisar_distribuicao(df: pd.DataFrame) -> str:
    idades = df["idade"]
    return (
        f"A idade média é **{idades.mean():.1f} anos** e a mediana é "
        f"**{idades.median():.0f} anos**. A maior concentração aparece nas "
        "faixas indicadas pelas barras mais altas."
    )


def analisar_frequencia(df: pd.DataFrame) -> str:
    frequencia = df["tipo_atendimento"].value_counts()
    tipo = frequencia.idxmax()
    percentual = frequencia.iloc[0] / frequencia.sum() * 100
    return (
        f"**{tipo}** é o tipo mais frequente, com {frequencia.iloc[0]} chamados "
        f"({percentual:.1f}% do total)."
    )


def analisar_heatmap(df: pd.DataFrame) -> str:
    tabela = df.pivot(
        index="dia_semana", columns="horario", values="movimento_clientes"
    )
    dia, horario = np.unravel_index(
        np.nanargmax(tabela.to_numpy()), tabela.shape
    )
    return (
        f"O maior movimento registrado ocorreu **{tabela.index[dia]} às "
        f"{tabela.columns[horario]}**, com {tabela.iloc[dia, horario]} clientes."
    )


def analisar_linhas(df: pd.DataFrame) -> str:
    medias = df.groupby("loja")["vendas"].mean()
    loja = medias.idxmax()
    return (
        f"**{loja}** teve a maior venda média no período "
        f"({formatar_valor(medias[loja])}). As linhas mostram a variação diária "
        "de cada loja."
    )


def analisar_pizza(df: pd.DataFrame) -> str:
    faturamento = df.groupby("canal_venda")["faturamento"].sum()
    canal = faturamento.idxmax()
    percentual = faturamento[canal] / faturamento.sum() * 100
    return (
        f"**{canal}** é o principal canal, com {percentual:.1f}% do faturamento "
        f"total ({formatar_valor(faturamento[canal])})."
    )


def analisar_regressao(df: pd.DataFrame) -> str:
    correlacao = df["renda_mensal"].corr(df["gasto_mensal"])
    return (
        f"A relação entre renda e gasto é positiva "
        f"(correlação de **{correlacao:.2f}**): rendas maiores tendem a acompanhar "
        "gastos maiores neste conjunto de dados."
    )


st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 3rem;}
    h1 {letter-spacing: -0.04em;}
    [data-testid="stMetricValue"] {font-size: 1.4rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 👤 Identificação do aluno")
    st.caption("Preencha seus dados para identificá-los no painel.")
    nome = st.text_input("Nome", placeholder="Seu nome completo")
    chamada = st.text_input("Número da chamada", placeholder="Ex.: 22400630")
    turma = st.text_input("Turma", placeholder="Ex.: 3D2")
    st.divider()
    st.markdown("**Aluno**")
    st.write(nome.strip() or "Não informado")
    st.markdown("**Número da chamada**")
    st.write(chamada.strip() or "Não informado")
    st.markdown("**Turma**")
    st.write(turma.strip() or "Não informado")

st.title("Painel de visualizações")
st.markdown(
    "Uma visão geral dos dados: nove gráficos organizados em três colunas, "
    "com uma breve análise para cada visualização."
)
st.divider()

try:
    dados = {
        "barras": carregar_dados("dados_barras.csv"),
        "boxplot": carregar_dados("dados_boxplot.csv"),
        "dispersao": carregar_dados("dados_dispersao.csv"),
        "distribuicao": carregar_dados("dados_distribuicao.csv"),
        "frequencia": carregar_dados("dados_frequencia.csv"),
        "heatmap": carregar_dados("dados_heatmap.csv"),
        "linhas": carregar_dados("dados_linhas.csv"),
        "pizza": carregar_dados("dados_pizza.csv"),
        "regressao": carregar_dados("dados_regressao.csv"),
    }
except (FileNotFoundError, pd.errors.ParserError) as erro:
    st.error(f"Não foi possível carregar os dados: {erro}")
    st.stop()

cartoes = [
    ("barras", criar_grafico_barras, analisar_barras),
    ("boxplot", criar_grafico_boxplot, analisar_boxplot),
    ("dispersao", criar_grafico_dispersao, analisar_dispersao),
    ("distribuicao", criar_grafico_distribuicao, analisar_distribuicao),
    ("frequencia", criar_grafico_frequencia, analisar_frequencia),
    ("heatmap", criar_grafico_heatmap, analisar_heatmap),
    ("linhas", criar_grafico_linhas, analisar_linhas),
    ("pizza", criar_grafico_pizza, analisar_pizza),
    ("regressao", criar_grafico_regressao, analisar_regressao),
]

for inicio in range(0, len(cartoes), 3):
    colunas = st.columns(3, gap="large")
    for coluna, (chave, criar_grafico, analisar) in zip(
        colunas, cartoes[inicio : inicio + 3]
    ):
        with coluna:
            with st.container(border=True):
                figura = criar_grafico(dados[chave])
                st.pyplot(figura, width="stretch")
                plt.close(figura)
                st.markdown("**Análise**")
                st.markdown(analisar(dados[chave]))