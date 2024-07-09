from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
API_KEY = os.getenv('api_key_openai')
ROOT_PATH = Path(__file__).parent / 'histories'

client = OpenAI(
    organization='org-o7HbJ1VY9N2rxRBBkYfnRypm',
    project='proj_ypBOj2fMCcpd5Eh0K6MbMWaT',
    api_key=API_KEY,
)

class NameGenerator:
    """
    Classe responsável por gerar nomes de personagens baseados em características fornecidas pelo usuário.
    """
    def __init__(self) -> None:
        pass

    def generate_name(self, characteristics: dict) -> str:
        """
        Gera um nome a partir das características de entrada do usuário.

        Args:
            characteristics (str): Uma string contendo as características desejadas para o nome do personagem.

        Returns:
            str: O nome gerado para o personagem.
        """
        # Processar características
        prompt = f"""
            Gerar um nome fantasia para um personagem de RPG com as seguintes características e me forneça apenas o nome:
            Idade: {characteristics["age"]}
            Gênero: {characteristics["gender"]}
            Personalidade: {characteristics["personality"]}
            Profissão: {characteristics["profession"]}
            Raça: {characteristics["race"]}
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                stream=False,
            )

            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Erro ao gerar o nome: {e}")
            return "Erro"
    
    def generate_history(self, name: str, characteristics: dict):
        prompt = f"""
            Crie uma breve historia para o personagem {name} e com as seguintes caracteristicas {characteristics}         
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                stream=False,
            )

            history_data = response.choices[0].message.content           
        
        except Exception as e:
            print(f"Erro ao gerar o nome: {e}")
            return "Erro"

        if not ROOT_PATH.exists():
            ROOT_PATH.mkdir(parents=True, exist_ok=True)
        
        history_path = ROOT_PATH / f'{name}.txt'

        with open(history_path, 'w') as file:
            file.write(history_data)

        return history_data
          
            
        
