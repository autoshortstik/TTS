# TTS ElevenLabs

Uma biblioteca simples para converter texto em áudio usando a API ElevenLabs.

## Instalação

```bash
pip install git+https://github.com/seu-usuario/TTS.git
```

## Configuração

Crie um arquivo `.env` na raiz do seu projeto com as seguintes variáveis:

```
API_KEY=sua_api_key_aqui
VOICE_ID=seu_voice_id_aqui
```

## Uso

```python
from tts_elevenlabs import text_to_speech

# Converter texto para áudio
text_to_speech("Este é um exemplo de texto para ser convertido em áudio.", 
               output_file="saida.mp3", 
               stability=0.5, 
               similarity_boost=0.75)
```