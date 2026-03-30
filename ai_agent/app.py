from agent_ai import car_sales_agent
import streamlit as st


# FRONT END
st.set_page_config(page_title="AI Data Analyst 🚗", page_icon="🤖")

st.title("🚗 Analista de Dados IA (AWS Athena)")
st.markdown("---")

query = st.text_input("Faça uma pergunta sobre as vendas (ex: Qual o total vendido por marca?):")

if query:
    with st.spinner("O Agente está consultando o Data Lake na AWS..."):
        # O Agno processa a pergunta, gera o SQL, roda no Athena e volta com a resposta
        response = car_sales_agent.run(query)
        st.markdown(response.content)

# Rodapé para o portfólio
st.sidebar.markdown("### Stack Tecnológica")
st.sidebar.write("🧠 gemini-2.5-flash")
st.sidebar.write("🤖 Agno (Agentic Framework)")
st.sidebar.write("☁️ Amazon S3 & Athena")
st.sidebar.write("🐍 Python & Boto3")