from dotenv import load_dotenv
import os
import sys

# Caminho para a raiz do projeto
raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if raiz not in sys.path:
    sys.path.append(raiz)

# AGENT
from aws.aws_athena_tool import run_athena_query
from agno.models.google import Gemini
from agno.agent import Agent

# Criar Gráficos
from typing import List
import streamlit as st
import pandas as pd


load_dotenv(os.path.join(raiz, '.env'))


def gerar_grafico_vendas(dados_lista: List[List[str]], titulo: str):
    """
    Recebe uma lista de listas (tabela) e exibe um gráfico de barras no Streamlit.
    O primeiro item da lista deve ser o cabeçalho.
    
    Args:
        dados_lista (List[List[str]]): Uma lista contendo as linhas da tabela.
        titulo (str): O título do gráfico.
    """
    try:
        import pandas as pd
        import streamlit as st
        
        # Transforma a lista do Athena [ AWS ] em um DataFrame real
        df = pd.DataFrame(dados_lista[1:], columns=dados_lista[0])
        
        # Converte colunas para número
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='ignore')
            
        st.write(f"### {titulo}")
        # Usa a primeira coluna como X e a segunda como Y
        st.bar_chart(data=df, x=df.columns[0], y=df.columns[1])
        
        return "Gráfico gerado com sucesso e exibido na tela."
    except Exception as e:
        return f"Erro ao gerar o gráfico: {str(e)}"

# Configuração do Agente
car_sales_agent = Agent(
    name="Analista de Vendas de Carros",
    model=Gemini(id="gemini-2.5-flash-lite"), # Mudar para quando atingir o limite FREE kkk
    tools=[run_athena_query, gerar_grafico_vendas],
    instructions=[
        "Você é um Analista de Dados Sênior.",
        "Sua tabela principal no Athena é 'ouro' no banco 'db_carros_etl'.",
        "As colunas são: id_venda, id_loja, modelo_carro, marca, valor, data_venda, nome_vendedor, nome_loja.",
        "REGRAS OBRIGATÓRIAS:",
        "1. Você DEVE SEMPRE usar a ferramenta 'run_athena_query' para executar o SQL na AWS.",
        "2. NUNCA responda apenas mostrando o código SQL. Você deve rodar a query, ler o resultado e responder a pergunta do usuário com os dados reais.",
        "3. Responda em Português do Brasil de forma direta, informando os valores encontrados.",
        "4. SE o usuário pedir um gráfico, visualização ou comparação visual, você DEVE chamar a ferramenta 'gerar_grafico_vendas' após obter os dados do Athena.",
        "5. Para o gráfico, escolha um título amigável e explicativo baseado na pergunta do usuário."
    ],
    markdown=True
)

if __name__ == "__main__":
    car_sales_agent.print_response("Qual o modelo de carro mais caro da tabela?")
