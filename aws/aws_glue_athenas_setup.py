from botocore.exceptions import ClientError
import boto3
import json
import time


# ==========================================
# 1. CONFIGURAÇÕES
# ==========================================
bucket_name = 'lojas-vendedores-carro-etl-projeto'
db_name = 'db_carros_etl'
crawler_name = 'crawler_vendas_ouro'
role_name = 'RoleGlueCrawlerCarros'

iam_client = boto3.client('iam')
glue_client = boto3.client('glue')

print("Iniciando configuração do AWS Glue via Boto3...\n")

# ==========================================
# 2. CRIANDO A PERMISSÃO (IAM ROLE)
# ==========================================
trust_relationship = {
    "Version": "2012-10-17",
    "Statement": [{"Effect": "Allow", "Principal": {"Service": "glue.amazonaws.com"}, "Action": "sts:AssumeRole"}]
}

try:
    print(f"Criando IAM Role '{role_name}' para o Glue...")
    iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_relationship)
    )
    # Dando permissão full para o S3 e permissões padrões do Glue
    iam_client.attach_role_policy(RoleName=role_name, PolicyArn='arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole')
    iam_client.attach_role_policy(RoleName=role_name, PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')
    
    print("⏳ Aguardando 10 segundos para a AWS propagar a permissão...")
    time.sleep(10)
    print("✅ Role criada com sucesso!\n")

except ClientError as e:
    if e.response['Error']['Code'] == 'EntityAlreadyExists':
        print(f"ℹ️ A Role '{role_name}' já existe. Seguindo em frente...\n")
    else:
        print(f"❌ Erro ao criar Role: {e}")
        exit()

role_arn = iam_client.get_role(RoleName=role_name)['Role']['Arn']

# ==========================================
# 3. CRIANDO O DATABASE NO GLUE
# ==========================================
try:
    print(f"Criando Database '{db_name}'...")
    glue_client.create_database(DatabaseInput={'Name': db_name})
    print("✅ Database criado!\n")
except ClientError as e:
    if e.response['Error']['Code'] == 'AlreadyExistsException':
        print(f"ℹ️ Database '{db_name}' já existe.\n")

# ==========================================
# 4. CRIANDO E INICIANDO O CRAWLER
# ==========================================
caminho_s3 = f's3://{bucket_name}/ouro/'

try:
    print(f"Criando Crawler '{crawler_name}' apontando para {caminho_s3}...")
    glue_client.create_crawler(
        Name=crawler_name,
        Role=role_arn,
        DatabaseName=db_name,
        Targets={'S3Targets': [{'Path': caminho_s3}]}
    )
    print("✅ Crawler criado!\n")
except ClientError as e:
    if e.response['Error']['Code'] == 'AlreadyExistsException':
        print(f"ℹ️ Crawler '{crawler_name}' já existe.\n")

print("🚀 Dando o comando de Start no Crawler...")
try:
    glue_client.start_crawler(Name=crawler_name)
    print("✅ Crawler iniciado com sucesso!")
    print("\n⏳ O Crawler leva de 1 a 2 minutos para ler os arquivos Parquet no S3 e criar a tabela.")
except ClientError as e:
    if e.response['Error']['Code'] == 'CrawlerRunningException':
        print("ℹ️ O Crawler já está rodando no momento.")