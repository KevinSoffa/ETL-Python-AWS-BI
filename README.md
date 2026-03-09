# Projeto ETL - Dados de Vendas de Carros (AWS & Power BI)

<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>

Este projeto consiste em um pipeline de dados ponta a ponta (ETL) que extrai dados de vendas de carros e lojas a partir de arquivos CSV, processa e transforma esses dados utilizando Python (Pandas) e armazena os resultados na AWS (S3) utilizando o padrão de arquitetura medalhão (Camadas Prata e Ouro). Os dados são catalogados via AWS Glue, consultados com AWS Athena e, por fim, consumidos por um dashboard no Power BI.

## 🏛️ Arquitetura do Projeto

![Diagrama da Arquitetura](img/seu_diagrama_aqui.png)

O fluxo de dados segue as seguintes etapas:

1. **Extração (CSV):** Os dados brutos de origem ficam na pasta `csv/`.
2. **Camada Prata (Transformação Inicial):** Notebooks Jupyter leem os CSVs, realizam a limpeza e o tratamento inicial dos dados, salvando os resultados no formato `.parquet` na pasta `parquet/`.
3. **Integração AWS (Boto3):** Scripts Python são responsáveis por fazer o upload dos dados da camada Prata para um bucket no Amazon S3. Em seguida, o AWS Glue e o Athena são configurados para criar o catálogo de dados e permitir consultas SQL.
4. **Camada Ouro (Consolidação):** Um notebook consome os dados tratados disponíveis no Athena/S3, realiza os joins e regras de negócios finais, e gera um arquivo consolidado `vendas_consolidadas_ouro.parquet`.
5. **Visualização:** O arquivo `.pbix` do Power BI consome os dados da camada Ouro para alimentar o dashboard de indicadores de vendas.

## 📂 Estrutura do Repositório

```text
DADOS_CARROS_AWS/
├── aws/                                # Scripts de infraestrutura e upload para AWS
│   ├── aws_glue_athenas_setup.py       # Configuração do banco e tabelas no Glue/Athena
│   ├── aws_s3_ouro.py                  # Upload/gerenciamento dos dados Ouro no S3
│   └── aws_s3_prata.py                 # Upload dos dados Prata para o S3
├── csv/                                # Arquivos de dados brutos (origem)
├── img/                                # Imagens de documentação e diagramas
├── notebook/                           # Notebooks de transformação de dados
│   ├── ouro/
│   │   └── lojas_vendas_ouro.ipynb     # Processamento e consolidação final
│   └── prata/
│       ├── lojas_vendedores_prata.ipynb # Tratamento de dados de lojas/vendedores
│       └── venda_carros_prata.ipynb     # Tratamento de dados de vendas
├── parquet/                            # Arquivos processados localmente
├── .env                                # Variáveis de ambiente (Credenciais AWS)
├── .gitignore                          # Arquivos ignorados pelo Git
└── dash_carros_AWS.pbix                # Dashboard do Power BI
```

## 🛠️ Tecnologias Utilizadas
Linguagem: Python (Pandas, Boto3)

Ambiente de Desenvolvimento: Jupyter Notebook

Nuvem (AWS): Amazon S3, AWS Glue, Amazon Athena

Armazenamento: Formato Parquet

Visualização: Power BI

## 🚀 Como Executar o ETL

Siga os passos abaixo para rodar o pipeline no seu ambiente local.

---

## 1️⃣ Pré-requisitos e Configuração

Certifique-se de ter o **Python instalado 3.12+**.  
Recomenda-se o uso de um **ambiente virtual (`.venv`)**.

### Instale as bibliotecas necessárias

```bash
pip install -r requirements.txt
```

