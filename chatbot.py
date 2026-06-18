from football_api import buscar_jogos_copa, formatar_jogos_para_gemini
from ia_api import perguntar_ia

def responder(pergunta):
    jogos = buscar_jogos_copa()
    contexto_jogos = formatar_jogos_para_gemini(jogos)

    return perguntar_ia(pergunta, contexto_jogos)