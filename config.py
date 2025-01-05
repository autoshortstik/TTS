import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Variáveis carregadas
API_KEY = os.getenv("API_KEY")
VOICE_ID = os.getenv("VOICE_ID")

# Verificação simples para garantir que as variáveis foram carregadas
if not API_KEY or not VOICE_ID:
    raise ValueError("Certifique-se de que as variáveis API_KEY e VOICE_ID estão definidas no arquivo .env")
