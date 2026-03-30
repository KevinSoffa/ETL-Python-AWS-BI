# Projeto ETL & AI Data Analyst - Vendas de Carros (AWS & Agno) 🚗🤖

<div align="center">
  <img height="150em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>

Este repositório apresenta uma solução de dados de ponta a ponta que integra um pipeline de **Engenharia de Dados (Arquitetura Medalhão)** com um **Agente de IA** capaz de realizar análises preditivas e visuais via linguagem natural.

---

## 📌 Sumário
* [🏛️ Arquitetura do Projeto](#-arquitetura-do-projeto)
* [📂 Estrutura do Repositório](#-estrutura-do-repositório)
* [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
* [🤖 Agente de IA (AI Data Analyst)](#-agente-de-ia-ai-data-analyst)
* [🚀 Como Executar o Projeto](#-como-executar-o-projeto)
* [📊 Dashboards (BI & IA)](#-dashboards-bi--ia)

---

## 🏛️ Arquitetura do Projeto

O fluxo de dados foi desenhado para garantir escalabilidade e baixo custo na AWS:

1. **Extração:** Coleta de dados brutos de vendas e lojas em formato CSV.  
2. **Camada Prata:** Limpeza, tipagem e tratamento inicial com **Python (Pandas)**, convertendo os arquivos para **Apache Parquet**.  
3. **Integração AWS:** Upload automatizado via **Boto3** para o **Amazon S3**. Catalogação automática via **AWS Glue** e criação de tabelas no **Amazon Athena**.  
4. **Camada Ouro:** Consolidação final, Joins de tabelas e aplicação de regras de negócio para consumo.  
5. **Consumo:** Visualização clássica via **Power BI** e consultas dinâmicas via **Agente de IA (Streamlit)**.

---

## 📂 Estrutura do Repositório

```text
DADOS_CARROS_AWS/
├── ai_agent/              # Módulo de Inteligência Artificial
│   ├── app.py             # Interface Streamlit do Agente
│   └── agent_ai.py        # Cérebro do Agente (Agno + Gemini)
├── aws/                   # Scripts de Infraestrutura e Ferramentas
│   ├── aws_athena_tool.py # Ferramenta que permite à IA ler o Athena
│   ├── aws_s3_ouro.py     # Gerenciamento da Camada Ouro no S3
│   └── aws_s3_prata.py    # Gerenciamento da Camada Prata no S3
├── notebook/              # Notebooks Jupyter de ETL (Pandas)
├── .env                   # Variáveis de ambiente (AWS e Google API)
└── dash_carros_AWS.pbix   # Dashboard Power BI
```

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12 (Pandas, Boto3)
- **Nuvem:** AWS (S3, Glue, Athena)
- **IA Generativa:** Agno Framework & Google Gemini 2.5 Flash
- **Visualização:** Streamlit, Plotly e Power BI

---

## 🤖 Agente de IA (AI Data Analyst)

O diferencial deste projeto é o **Analista de Dados IA**, que utiliza o modelo **Google Gemini** como motor de inteligência e o **framework Agno (Phidata)** para orquestração de ferramentas e agentes.  

Ele atua como um assistente inteligente que **conversa diretamente com o Data Lake** e transforma perguntas em análises reais.

### 🔹 Como o agente funciona

- **Modelo de Linguagem:**  
  Google Gemini 2.5 — responsável pelo raciocínio lógico, interpretação de perguntas e geração automática de SQL.

- **Framework de Agentes:**  
  Agno (Phidata) — responsável pela orquestração de ferramentas, execução de consultas e interface de chat.

- **Processamento Inteligente:**  
  O agente interpreta a pergunta do usuário, gera automaticamente o SQL Presto, executa a consulta no **Amazon Athena (AWS)** e recebe os dados brutos.

- **Saída Inteligente:**  
  O agente decide automaticamente se:
  - responde apenas em texto, ou  
  - utiliza a ferramenta de visualização para gerar **gráficos dinâmicos no Streamlit**.

---

### 💡 Diferencial do Projeto

Esse ajuste mostra que o projeto não apenas utiliza IA, mas aplica **engenharia de agentes de forma prática**, escolhendo as ferramentas certas:

**Gemini + Agno + Athena + Streamlit**

Ou seja, não é apenas um chatbot — é um **AI Data Analyst funcional integrado a um Data Lake real** 🚀

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/KevinSoffa/DADOS_CARROS_AWS.git
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o arquivo `.env`
Adicione suas chaves:

```env
CAMINHO_DIRETORIO_PARQUET=xxxx
CAMINHO_DIRETORIO_ENV=xxxx
CAMINHO_DIRETORIO_CSV=xxxx

# AWS
S3_OURO=xxxx

# GEMINI
GOOGLE_API_KEY=xxxx
```

### 4. Inicie o Agente
```bash
streamlit run ai_agent/app.py
```

---

## 📊 Dashboards (BI & IA)

### IA Analyst (Streamlit + Plotly)
O agente interpretando dados e gerando visualizações automáticas em tempo real.

### Business Intelligence (Power BI)
Visão executiva e estática dos principais indicadores de vendas.

---

## 👨‍💻 Autor

**Kevin Soffa**

- [LinkedIn](https://www.linkedin.com/in/kevin-soffa-da-silva-souza-2607b5212/)
- [GitHub](https://github.com/KevinSoffa)