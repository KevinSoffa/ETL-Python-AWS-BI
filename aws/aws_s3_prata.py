from botocore.exceptions import ClientError
from decouple import config
import boto3
import os


# ==========================================
# CONFIGURAÇÕES DE DIRETÓRIO E AWS
# ==========================================
diretorio_base = config("CAMINHO_DIRETORIO_PARQUET")
caminho_vendas = os.path.join(diretorio_base, "vendas_carros_prata.parquet")
caminho_lojas = os.path.join(diretorio_base, "lojas_vendedores_prata.parquet")

session = boto3.session.Session()
regiao_aws = session.region_name
s3_client = boto3.client('s3')

bucket_name = 'lojas-vendedores-carro-etl-projeto'

# ==========================================
# FUNÇÃO PARA CRIAR/VERIFICAR O BUCKET
# ==========================================
def criar_bucket(nome_bucket, regiao):
    try:
        print(f"Verificando o bucket '{nome_bucket}' na região {regiao}...")
        
        if regiao == 'us-east-1' or regiao is None:
            s3_client.create_bucket(Bucket=nome_bucket)
        else:
            s3_client.create_bucket(
                Bucket=nome_bucket,
                CreateBucketConfiguration={'LocationConstraint': regiao}
            )
        print("✅ Bucket pronto para uso!\n")
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'BucketAlreadyOwnedByYou':
            print("ℹ️ O bucket já existe na sua conta. Seguindo para o upload...\n")
        elif error_code == 'BucketAlreadyExists':
            print(f"❌ ERRO FATAL: O nome '{nome_bucket}' já é usado por outra pessoa na AWS.")
            exit()
        else:
            print(f"❌ Erro ao tentar criar o bucket: {e}")
            exit()

# ==========================================
# FUNÇÃO DE UPLOAD [ com UPDATED ]
# ==========================================
def upload_to_s3_otimizado(file_path, bucket, object_name):
    try:
        print(f"Iniciando upload/atualização de: {file_path}")
        s3_client.upload_file(
            Filename=file_path,
            Bucket=bucket,
            Key=object_name,
            ExtraArgs={'StorageClass': 'INTELLIGENT_TIERING'}
        )
        print(f"✅ Atualização concluída: s3://{bucket}/{object_name}\n")
        
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo não foi encontrado: {file_path}")
    except ClientError as e:
        print(f"❌ Erro na AWS ao subir {file_path}: {e}")

# ==========================================
# EXECUÇÃO DO FLUXO
# ==========================================
print("Iniciando pipeline de Upload AWS (Modo Substituição)...\n")

criar_bucket(nome_bucket=bucket_name, regiao=regiao_aws)

upload_to_s3_otimizado(
    file_path=caminho_vendas, 
    bucket=bucket_name, 
    object_name='prata/vendas/vendas_carros_prata.parquet'
)

upload_to_s3_otimizado(
    file_path=caminho_lojas, 
    bucket=bucket_name, 
    object_name='prata/lojas/lojas_vendedores_prata.parquet'
)
