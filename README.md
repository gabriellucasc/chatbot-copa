# 🌎 Chatbot da Copa do Mundo

Chatbot inteligente desenvolvido para a disciplina de Inteligência Artificial da Universidade Estadual de Santa Cruz (UESC).

O sistema combina uma API de dados esportivos em tempo real com um Modelo de Linguagem de Grande Escala (LLM), permitindo responder perguntas históricas sobre Copas do Mundo e consultas atualizadas sobre partidas, placares e calendário da competição.

---

## 🚀 Funcionalidades

### 📚 Perguntas históricas

O chatbot utiliza a API Gemini para responder perguntas relacionadas à história da Copa do Mundo.

Exemplos:

* Quem foi campeão da Copa do Mundo de 2002?
* Quem marcou o gol da final de 2014?
* Quantos títulos mundiais o Brasil possui?
* Qual seleção venceu a Copa de 2018?
* Quem foi o artilheiro da Copa de 2006?

### ⚽ Dados em tempo real

O sistema utiliza a API Football-Data para obter informações atualizadas da Copa do Mundo.

Exemplos:

* Qual o próximo jogo do Brasil?
* Quais são os próximos jogos da Copa?
* Quais partidas acontecem hoje?
* Qual foi o placar do último jogo da Argentina?
* Quando a França joga novamente?

---

## 🧠 Arquitetura do Sistema

O chatbot utiliza uma abordagem semelhante a Retrieval-Augmented Generation (RAG).

Fluxo de funcionamento:

Usuário → Streamlit → Football-Data API → Gemini → Resposta

1. O usuário envia uma pergunta.
2. O sistema consulta a API Football-Data para obter os dados atualizados das partidas.
3. Os dados são transformados em texto.
4. O contexto é enviado juntamente com a pergunta para a API Gemini.
5. O Gemini interpreta os dados e gera uma resposta em linguagem natural.

---

## 🛠️ Tecnologias Utilizadas

* Python 3.13
* Streamlit
* Google Gemini API
* Football-Data API
* Requests
* Python Dotenv

---

## 📂 Estrutura do Projeto

```text
chatbot-copa/
│
├── app.py
├── chatbot.py
├── football_api.py
├── ia_api.py
├── .env
├── requirements.txt
└── README.md
```

### Arquivos

| Arquivo          | Descrição                    |
| ---------------- | ---------------------------- |
| app.py           | Interface gráfica do chatbot |
| chatbot.py       | Coordena o fluxo entre APIs  |
| football_api.py  | Consome a API Football-Data  |
| ia_api.py        | Comunicação com a API Gemini |
| .env             | Armazena as chaves das APIs  |
| requirements.txt | Dependências do projeto      |

---

## 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
FOOTBALL_DATA_TOKEN=SUA_CHAVE_FOOTBALL_DATA

GEMINI_API_KEY=SUA_CHAVE_GEMINI
```

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/gabriellucasc/chatbot-copa.git
```

Entre na pasta:

```bash
cd chatbot-copa
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Execução

Execute o Streamlit:

```bash
streamlit run app.py
```

O sistema ficará disponível em:

```text
http://localhost:8501
```

---

## 💬 Exemplos de Uso

### Histórico

```text
Quem foi campeão da Copa de 2002?
```

```text
Quem marcou o gol da final de 2014?
```

### Jogos atuais

```text
Qual o próximo jogo do Brasil?
```

```text
Quais são os próximos jogos da Copa?
```

```text
Qual foi o placar do jogo da Argentina?
```

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido como trabalho final da disciplina de Inteligência Artificial da Universidade Estadual de Santa Cruz (UESC), com o objetivo de demonstrar a integração entre APIs externas, modelos de linguagem e sistemas conversacionais inteligentes.

---

## 👨‍💻 Autores

Gabriel César, Isabella Secchin, Ronaldo Porto Filho

Curso: Ciência da Computação – UESC

Disciplina: Inteligência Artificial