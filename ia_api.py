import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def perguntar_ia(pergunta, contexto_jogos=""):
    prompt = f"""
Você é um chatbot especializado em Copa do Mundo.

Você deve responder em português, de forma clara e objetiva.

Use os dados de jogos fornecidos abaixo quando a pergunta for sobre:
- próximos jogos;
- jogos de hoje;
- placares;
- datas;
- partidas específicas;
- seleções na Copa.

IMPORTANTE:
- Para perguntas sobre partidas, datas, horários, placares e seleções,
utilize SOMENTE os dados fornecidos pela API.
- Use horário de Brasília (UTC-3) nas respostas.
- Não invente jogos.
- Não invente placares.
- Se a informação não estiver nos dados, diga que não encontrou.

Se a pergunta for histórica, como campeões, gols de finais, sedes ou curiosidades,
responda usando seu conhecimento geral sobre Copa do Mundo.

Dados atuais da API football-data:
{contexto_jogos}

Pergunta do usuário:
{pergunta}
"""

    try:
        resposta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return resposta.text

    except Exception as erro:
        print(f"Erro Gemini: {erro}")

        return """
⚠️ A API Gemini está temporariamente indisponível ou a cota foi excedida.

Tente novamente em alguns minutos.
"""