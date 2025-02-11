# README

## Descrição

Este repositório contém um script Python que automatiza o processo de download, transcrição e resumo de vídeos do YouTube. O script utiliza as bibliotecas `yt-dlp` para baixar o áudio, `speech_recognition` para transcrever o áudio para texto, e a API da OpenAI (GPT-4) para melhorar a transcrição ou gerar um resumo do conteúdo. O fluxo completo permite baixar um vídeo do YouTube, transcrever seu áudio para texto e, em seguida, escolher entre obter a transcrição corrigida ou um resumo conciso do conteúdo.

## Funcionalidades

- **Baixar Áudio do YouTube**: O script baixa o áudio de vídeos do YouTube em formato MP3.
- **Converter MP3 para WAV**: O áudio baixado é convertido de MP3 para WAV, formato necessário para transcrição.
- **Transcrição de Áudio**: O áudio convertido para WAV é transcrito para texto utilizando a API do Google Speech Recognition.
- **Correção de Texto ou Resumo**: O texto transcrito é enviado à API da OpenAI para correção ortográfica ou resumo.
- **Opções de Resumo ou Transcrição Completa**: O usuário pode escolher entre obter a transcrição corrigida ou um resumo conciso do conteúdo.

## Pré-requisitos

- Python 3.7 ou superior.
- As bibliotecas `yt-dlp`, `speech_recognition`, `pydub` e `openai` precisam estar instaladas.
- FFmpeg deve estar instalado e configurado no sistema.

Para instalar o projeto, siga os passos abaixo: 

1. Clone o repositório utilizando o comando `git clone https://github.com/usuario/repo.git` e navegue até o diretório do projeto.
2. Crie e ative um ambiente virtual (opcional, mas recomendado).
3. Instale as dependências com `pip install -r requirements.txt` ou manualmente com `pip install yt-dlp speechrecognition pydub openai`.
4. Instale o FFmpeg em [ffmpeg.org](https://ffmpeg.org/download.html) e adicione o caminho do executável ao seu sistema.

## Configuração

Para configurar o projeto, insira sua chave da API da OpenAI no código, obtendo-a em [platform.openai.com](https://platform.openai.com/). Substitua no código `openai.api_key = 'Insira sua CHAVE OPENAI AQUI'`. Certifique-se de que o FFmpeg está instalado corretamente e configure o caminho do executável no código.

## Como Usar

Para executar o script, utilize o comando `python script.py`. O script solicitará a URL de um vídeo do YouTube, baixará o áudio em MP3, converterá para WAV e transcreverá o áudio para texto. Você poderá escolher entre obter a transcrição completa corrigida ou um resumo conciso do conteúdo. Durante a execução, você verá opções para escolher entre transcrição completa, resumo ou sair do programa.

## Exemplo de Saída

Após a execução, você verá mensagens indicando o progresso, como "Download concluído com sucesso", "Arquivo MP3 convertido para WAV com sucesso" e "Texto transcrito com sucesso". O script também pedirá que você escolha entre transcrição completa ou resumo.

## Contribuição

Se você deseja contribuir com melhorias ou correções, sinta-se à vontade para abrir um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

**Nota**: O código foi desenvolvido para fins educacionais e automação de tarefas relacionadas à transcrição e resumo de vídeos. O uso de APIs de terceiros, como OpenAI e Google Speech Recognition, está sujeito às respectivas políticas de uso.
