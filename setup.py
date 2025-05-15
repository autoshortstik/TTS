from setuptools import setup, find_packages

setup(
    name="tts-elevenlabs",
    version="0.1.0",
    description="Biblioteca para conversão de texto para áudio usando a API ElevenLabs",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    python_requires=">=3.6",
)