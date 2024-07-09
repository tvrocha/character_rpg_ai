from dotenv import load_dotenv
from pathlib import Path
import openai
import os
import random

load_dotenv()
API_KEY = os.getenv('api_key_openai')
ROOT_PATH = Path(__file__).parent / 'voices'

openai.api_key = API_KEY

class VoiceGenerator:

    # Gerar uma voz a partir das caracteristicas de entrada do Usuário
    def generate_voice(self, name: str, characteristics: dict, history: str):
        male_voice = ['echo', 'onyx']
        female_voice = ['alloy', 'fable', 'nova', 'shimmer']

        if characteristics["gender"][0].lower() == "m":
            voice = random.choice(male_voice)
        else:
            voice = random.choice(female_voice)
        
        response = openai.audio.speech.create(
            model='tts-1-hd',
            voice=voice,
            input=history,
        )

        if not ROOT_PATH.exists():
            ROOT_PATH.mkdir(parents=True, exist_ok=True)
        
        audio_path = ROOT_PATH / f'{name}.mp3'

        response.stream_to_file(audio_path)

        print(f'\nAudio salvo em: {audio_path}')
        

        