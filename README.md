# Gerador de Personagens de RPG com IAs Generativas

## 📒 Descrição
Este projeto visa criar um personagem de RPG completo gerando seu nome, história, voz e avatar utilizando tecnologias de IAs generativas. O objetivo é explorar o potencial dessas ferramentas para criar conteúdos realistas e imersivos.

## 🤖 Tecnologias Utilizadas
- **GPT-3.5**: Para a geração de nomes e descrições de personagens.
- **OpenAI (TTS)**: Para a geração de voz com base nas características definidas pelo usuário.
- **DALL-E**: Para a criação de avatares visuais dos personagens.
- **Python**: Para a integração de todas as partes do projeto.

## 🧐 Processo de Criação
1. **Geração de Nome**:
   - Utilizamos o modelo GPT-4 para criar nomes únicos e coerentes para os personagens com base em características fornecidas pelo usuário.
2. **Geração de Voz**:
   - Com o TTS do OpenAI, geramos a voz do personagem conforme as especificações de gênero.
3. **Criação do Avatar**:
   - Usando o DALL-E, geramos imagens de avatares que representam visualmente os personagens de acordo com as descrições fornecidas.
4. **Integração**:
   - Implementamos um script em Python para orquestrar a comunicação entre as diferentes APIs, gerando o nome, voz e avatar de forma coesa e automatizada.

## 🚀 Resultados
- **Nome**: "Sylvana Fireheart"
- **Voz**: Um áudio gerado descrevendo a história do personagem com uma voz feminina e imponente.
- **Avatar**: Uma imagem de um arqueira elfa.

## Localização dos Arquivos Gerados

Após a execução do código, os arquivos gerados são armazenados nos seguintes diretórios:

- **Textos Gerados:** Os arquivos de texto com as histórias dos personagens são salvos no diretório `histories`. Cada arquivo é nomeado com o nome do personagem, seguido da extensão `.txt`.

- **Áudios Gerados:** Os arquivos de áudio com as vozes dos personagens são salvos no diretório `voices`. Cada arquivo de áudio é nomeado com o nome do personagem, seguido da extensão `.mp3`.

- **Imagens Geradas:** As imagens dos avatares dos personagens são salvas no diretório `images`. Cada imagem é nomeada com o nome do personagem, seguido da extensão `.png`.

Certifique-se de verificar esses diretórios após a execução do código para acessar os arquivos gerados para cada personagem criado.

## 💭 Reflexão 
Integrar tecnologias como GPT-3.5, TTS da OpenAI e DALL-E para criar um Gerador de Personagens de RPG foi uma experiência fascinante e esclarecedora. Além de permitir a criação de avatares visualmente expressivos, histórias emocionantes, vozes distintas e personagens com nomes exclusivos, essas ferramentas também abordaram questões técnicas como a integração de APIs e ajustes de parâmetros para garantir realismo e coerência nos resultados. O projeto enfatizou a importância de equilibrar a criatividade humana com a automação para garantir qualidade e originalidade, mostrando quais são as limitações da automação criativa e enfatizando a importância da criatividade humana no processo de criação digital.

