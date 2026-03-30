from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("🚗 TODOS os modelos liberados para a sua chave:")
print("-" * 40)

# Sem filtros agora, vai imprimir tudo!
try:
    for m in client.models.list():
        print(f"-> {m.name}")
except Exception as e:
    print(f"Erro ao buscar modelos: {e}")