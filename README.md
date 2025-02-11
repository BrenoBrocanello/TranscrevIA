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

## Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
