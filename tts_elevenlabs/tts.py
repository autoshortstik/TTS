import requests
from .config import API_KEY, VOICE_ID

def text_to_speech(texto, output_file="output.mp3", stability=0.5, similarity_boost=0.75):
    """
    Converte texto para áudio usando a API ElevenLabs
    
    Args:
        texto (str): Texto a ser convertido em áudio
        output_file (str): Nome do arquivo de saída
        stability (float): Valor de estabilidade (0.0 a 1.0)
        similarity_boost (float): Valor de similaridade (0.0 a 1.0)
        
    Returns:
        bool: True se a conversão foi bem sucedida, False caso contrário
    """
    # URL da API ElevenLabs para sintetização de voz
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

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
            "stability": stability,
            "similarity_boost": similarity_boost
        }
    }

    # Fazendo a requisição POST para a API
    response = requests.post(url, headers=headers, json=data)

    # Salvando o áudio como um arquivo MP3
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Áudio salvo como '{output_file}'")
        return True
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return False