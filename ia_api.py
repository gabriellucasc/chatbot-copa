import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def formatar_historico(historico):
    linhas = []

    for mensagem in historico:
        papel = mensagem.get("papel", "")
        conteudo = mensagem.get("conteudo", "")

        if papel == "user":
            linhas.append(f"Usuário: {conteudo}")
        elif papel == "assistant":
            linhas.append(f"Chatbot: {conteudo}")

    return "\n".join(linhas)


def perguntar_ia(pergunta, contexto_jogos="", historico=None):
    if historico is None:
        historico = []

    historico_formatado = formatar_historico(historico)

    prompt = f"""
Você é um chatbot especializado em Copa do Mundo.

Você deve responder em português, de forma clara e objetiva.

Use o histórico da conversa para entender referências como:
- "esse jogo";
- "essa seleção";
- "o próximo";
- "e o placar?";
- "quando vai ser?";
- "contra quem?".

Histórico da conversa:
{historico_formatado}

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
- Se a pergunta atual depender do histórico, use a conversa anterior para entender o contexto.
- Se a pergunta atual fizer referência a um ano mencionado no histórico, use esse ano como contexto principal.
- Não interprete "esse ano" como 2026 automaticamente quando houver outro ano citado na conversa anterior.

Se a pergunta for histórica, como campeões, gols de finais, sedes ou curiosidades,
responda usando seu conhecimento geral sobre Copa do Mundo.

Se o usuário usar expressões como:
- "nesse ano";
- "naquele ano";
- "essa Copa";
- "essa edição";
- "e a atual?";

interprete essas expressões com base no histórico da conversa antes de responder.

Dados atuais da API football-data:
{contexto_jogos}

Pergunta atual do usuário:
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