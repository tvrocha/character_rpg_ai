from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import requests

load_dotenv()
API_KEY = os.getenv('api_key_openai')
ROOT_PATH = Path(__file__).parent / 'images'

client = OpenAI(
    organization='org-o7HbJ1VY9N2rxRBBkYfnRypm',
    project='proj_ypBOj2fMCcpd5Eh0K6MbMWaT',
    api_key=API_KEY,
)

class CharacterGenerator:

    # Gerar um personagem a partir das características do Usuário
    def generate_character(self, name:str, history: str):

        prompt_historia = f"""Baseado na história abaixo, me responda com uma breve apresentação focada nas caracteristicas fisicas e/ou na personalidade do personagem.
        Historia: {history}
        """

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt_historia
                    }
                ],
                stream=False,
            )

            resumo_history = response.choices[0].message.content
        
        except Exception as e:
            print(f"Erro ao gerar o nome: {e}")
            return "Erro"       

        prompt = f'A partir deste resumo, crie a imagem do personagem: {resumo_history}'

        response = client.images.generate(
            model='dall-e-3',
            prompt=prompt, n=1,
            size='1024x1024'
        )

        image_url = response.data[0].url
        image_data = requests.get(image_url).content

        if not ROOT_PATH.exists():
            ROOT_PATH.mkdir(parents=True, exist_ok=True)

        image_path = ROOT_PATH / f'{name}.png'

        with open(image_path, 'wb') as file:
            file.write(image_data)
        
        print(f'\nImagem salva em: {image_path}')

        