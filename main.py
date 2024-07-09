from character.models import CharacterGenerator
from voice.models import VoiceGenerator
from name.models import NameGenerator


def main():

    # Caracaterísticas do personagem
    characteristics = {
        "name": "",
        "age": 23,
        "gender": "Feminino",
        "personality": "Filha do rei dos orcs e excelente médica",
        "profession": "médica militar",
        "race": "Orc",
    }

    name_generator = NameGenerator()  
    nome = name_generator.generate_name(characteristics)
    historia = name_generator.generate_history(nome, characteristics)
    print(f'Nome: {nome}\n\n{historia}')

    voice_generator = VoiceGenerator()
    voice_generator.generate_voice(nome, characteristics, historia)

    character_generator = CharacterGenerator()
    character_generator.generate_character(nome, historia)
    


if __name__ == "__main__":
    main()

