import boto3
import time


def run_athena_query(query: str):
    """
    Executa uma query SQL no Amazon Athena e retorna os resultados em formato de lista.
    """
    client = boto3.client('athena')
    
    DATABASE = "db_carros_etl" 
    S3_OUTPUT = "s3://lojas-vendedores-carro-etl-projeto/athena-results/"

    # 1. Inicia a consulta
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': DATABASE},
        ResultConfiguration={'OutputLocation': S3_OUTPUT}
    )
    
    id_execucao = response['QueryExecutionId']
    
    # 2. Aguarda a consulta finalizar
    while True:
        status_response = client.get_query_execution(QueryExecutionId=id_execucao)
        status = status_response['QueryExecution']['Status']['State']
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        time.sleep(1)

    # 3. Se sucesso, BUSCA E FORMATA OS DADOS
    if status == 'SUCCEEDED':
        results = client.get_query_results(QueryExecutionId=id_execucao)
        rows = results['ResultSet']['Rows']
        
        if not rows:
            return "A query rodou com sucesso, mas retornou zero linhas."

        # Criamos uma lista de listas (formato de tabela)
        tabela_dados = []
        for row in rows:
            # Extrai o valor de cada célula. Se estiver vazio, vira '0'
            linha = [col.get('VarCharValue', '0') for col in row['Data']]
            tabela_dados.append(linha)
            
        # Retornamos a lista pura. O Agente vai saber usar isso para o gráfico.
        return tabela_dados
        
    else:
        motivo = status_response['QueryExecution']['Status'].get('StateChangeReason', 'Erro desconhecido')
        return f"Falha na consulta ao Athena: {status}. Motivo: {motivo}"