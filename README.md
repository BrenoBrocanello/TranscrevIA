Este repositório contém um script Python que automatiza o processo de download, transcrição e resumo de vídeos do YouTube. O script utiliza as bibliotecas yt-dlp para baixar o áudio, speech_recognition para transcrever o áudio para texto, e a API da OpenAI (GPT-4) para melhorar a transcrição ou gerar um resumo do conteúdo. O fluxo completo permite baixar um vídeo do YouTube, transcrever seu áudio para texto e, em seguida, escolher entre obter a transcrição corrigida ou um resumo conciso do conteúdo.

Funcionalidades
Baixar Áudio do YouTube: O script baixa o áudio de vídeos do YouTube em formato MP3.
Converter MP3 para WAV: O áudio baixado é convertido de MP3 para WAV, formato necessário para transcrição.
Transcrição de Áudio: O áudio convertido para WAV é transcrito para texto utilizando a API do Google Speech Recognition.
Correção de Texto ou Resumo: O texto transcrito é enviado à API da OpenAI para correção ortográfica ou resumo.
Opções de Resumo ou Transcrição Completa: O usuário pode escolher entre obter a transcrição corrigida ou um resumo conciso do conteúdo.
Pré-requisitos
Python 3.7 ou superior.
As bibliotecas yt-dlp, speech_recognition, pydub e openai precisam estar instaladas.
FFmpeg deve estar instalado e configurado no sistema.
Instalação
Clone o repositório

bash
Copiar
git clone https://github.com/usuario/repo.git
cd repo
Instale as dependências

Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar
python -m venv venv
source venv/bin/activate  # Para Windows, use venv\Scripts\activate
Em seguida, instale as dependências:

bash
Copiar
pip install -r requirements.txt
Ou instale as bibliotecas manualmente:

bash
Copiar
pip install yt-dlp speechrecognition pydub openai
Instale o FFmpeg

Baixe o FFmpeg em: https://ffmpeg.org/download.html
Adicione o caminho do executável do FFmpeg ao ambiente do sistema (no código, o caminho do FFmpeg é configurado em ffmpeg_path).
Configuração
Chave da API OpenAI:

Insira sua chave da API da OpenAI para utilizar o GPT-4. Você pode obter sua chave na plataforma da OpenAI: https://platform.openai.com/

Substitua no código:

python
Copiar
openai.api_key = 'Insira sua CHAVE OPENAI AQUI'
Configuração do FFmpeg:

Certifique-se de que o FFmpeg está instalado corretamente e configure o caminho do executável no código:

python
Copiar
ffmpeg_path = r'Caminho\Para\FFmpeg\bin\ffmpeg.exe'  # Substitua pelo caminho correto
Como Usar
Executando o Script

Para rodar o script, execute o arquivo Python:

bash
Copiar
python script.py
Fluxo de Execução

O script seguirá o seguinte fluxo:

Solicitará a URL de um vídeo do YouTube para download.
Baixará o áudio do vídeo em formato MP3.
Converterá o MP3 para WAV.
Transcreverá o áudio para texto usando o Google Speech Recognition.
Você poderá escolher entre obter a transcrição completa corrigida ou um resumo conciso do conteúdo.
Opções no Terminal

Durante a execução, você será solicitado a escolher entre:

1 para obter a transcrição completa corrigida.
2 para gerar um resumo do conteúdo.
3 para sair do programa.
Exemplo de Saída
Após o processo ser completado, você verá uma saída como esta:

bash
Copiar
 ✅ Download concluído com sucesso ✅
 ✅ Arquivo MP3 convertido para WAV com sucesso! ✅
 ✅ Arquivo MP3 excluído com sucesso! ✅
 📝 Aguarde enquanto fazemos a transcrição do áudio...
 ✅ Texto transcrito com sucesso ✅
Você deseja a transcrição do vídeo completa ou um resumo? 
1️⃣ - Transcrição Completa  
2️⃣ - Resumo 
3️⃣ - Sair do programa: 1
Aguarde enquanto carregamos a transcrição completa...
Texto corrigido: [Texto corrigido pela OpenAI]
Contribuição
Se você deseja contribuir com melhorias ou correções, sinta-se à vontade para abrir um pull request.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Nota: O código foi desenvolvido com fins educacionais e para fins de automação de tarefas relacionadas à transcrição e resumo de conteúdo de vídeos. O uso de APIs de terceiros como OpenAI e Google Speech Recognition está sujeito às respectivas políticas de uso e limitações.
