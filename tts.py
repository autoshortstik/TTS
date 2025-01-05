import requests
from config import API_KEY, VOICE_ID  # Importa as variáveis do config.py

# URL da API ElevenLabs para sintetização de voz
url = "https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

# Texto que será transformado em áudio
texto = "Bom dia Este é um teste de conversão de texto para áudio usando a API do ElevenLabs."

# Cabeçalhos da requisição
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

# Dados da requisição (o texto e algumas configurações)
data = {
    "text": texto,
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

# Fazendo a requisição POST para a API
response = requests.post(url.format(VOICE_ID=VOICE_ID), headers=headers, json=data)

# Salvando o áudio como um arquivo MP3
if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("Áudio salvo como 'output.mp3'")
else:
    print(f"Erro: {response.status_code} - {response.text}")
