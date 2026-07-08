import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("FOOTBALL_DATA_TOKEN")
BASE_URL = "https://api.football-data.org/v4"

headers = {"X-Auth-Token": TOKEN}


def buscar_jogos_copa():
    url = f"{BASE_URL}/competitions/WC/matches"

    try:
        resposta = requests.get(url, headers=headers, timeout=15)

        if resposta.status_code != 200:
            return []

        dados = resposta.json()
        return dados.get("matches", [])

    except requests.exceptions.RequestException:
        return []


def traduzir_status(status):
    status_traduzido = {
        "SCHEDULED": "Agendado",
        "TIMED": "Com horário definido",
        "IN_PLAY": "Em andamento",
        "PAUSED": "Intervalo",
        "FINISHED": "Finalizado",
        "POSTPONED": "Adiado",
        "SUSPENDED": "Suspenso",
        "CANCELED": "Cancelado"
    }

    return status_traduzido.get(status, status)


def formatar_jogos_para_gemini(jogos):
    linhas = []

    for jogo in jogos:
        data = jogo.get("utcDate", "Data não informada")

        status_original = jogo.get("status", "Status não informado")
        status = traduzir_status(status_original)

        casa = jogo.get("homeTeam", {}).get("name") or "A definir"
        fora = jogo.get("awayTeam", {}).get("name") or "A definir"

        placar_casa = jogo.get("score", {}).get("fullTime", {}).get("home")
        placar_fora = jogo.get("score", {}).get("fullTime", {}).get("away")

        if placar_casa is None or placar_fora is None:
            placar = "sem placar"
        else:
            placar = f"{placar_casa}x{placar_fora}"

        linhas.append(
            f"Data: {data} | Status: {status} | Jogo: {casa} x {fora} | Placar: {placar}"
        )

    return "\n".join(linhas)