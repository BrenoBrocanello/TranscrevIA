import yt_dlp
import speech_recognition as sr
import os
from pydub import AudioSegment
import openai

# Configuração da API da OpenAI
# Insira sua chave da API da OpenAI abaixo. Você pode obtê-la em: https://platform.openai.com/
openai.api_key = 'Insira sua CHAVE OPENAI AQUI'  # Substitua pelo seu valor

# Configuração do FFmpeg
# Certifique-se de que o FFmpeg está instalado e adicione o caminho do executável abaixo.
# Baixe o FFmpeg em: https://ffmpeg.org/
ffmpeg_path = r'Caminho\Para\FFmpeg\bin\ffmpeg.exe'  # Substitua pelo caminho correto
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)
AudioSegment.converter = ffmpeg_path

def baixar_mp3_youtube():
    """
    Baixa o áudio de um vídeo do YouTube em formato MP3.
    O arquivo será salvo no diretório atual do script.
    """
    url = input('Coloque a URL do vídeo que deseja o resumo (ex: "https://www.youtube.com/watch?v=y6120QOlsfU"): ')

    # Define o diretório de destino para o download (usando o diretório atual)
    output_path = os.path.join(os.getcwd(), '%(title)s.%(ext)s')

    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,  # Usa o caminho do FFmpeg configurado
        'format': 'bestaudio/best',
        'outtmpl': output_path,  # Salva o arquivo no diretório atual
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(' ✅ Download concluído com sucesso ✅')

def converter_mp3_para_wav(mp3_path):
    """
    Converte o arquivo MP3 para WAV, que é o formato necessário para a transcrição.
    Remove o arquivo MP3 após a conversão.
    """
    wav_path = mp3_path.replace('.mp3', '.wav')
    audio = AudioSegment.from_mp3(mp3_path)

    # Configurações para garantir o formato correto (16 kHz, mono)
    audio = audio.set_frame_rate(16000)  # Taxa de amostragem de 16 kHz
    audio = audio.set_channels(1)       # Mono
    audio.export(wav_path, format="wav", parameters=["-ac", "1", "-ar", "16000"])

    # Remove o arquivo MP3 após a conversão
    os.remove(mp3_path)
    print(' ✅ Arquivo MP3 convertido para WAV com sucesso! ✅')
    print(' ✅ Arquivo MP3 excluído com sucesso! ✅')
    print(" 📝 Aguarde enquanto fazemos a transcrição do áudio...")

    return wav_path

def transcrever_audio(mp3_path):
    """
    Transcreve o áudio do arquivo MP3 para texto usando o Google Speech Recognition.
    Remove o arquivo WAV após a transcrição.
    """
    wav_path = converter_mp3_para_wav(mp3_path)

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as audio_file:
        audio_data = recognizer.record(audio_file)

    try:
        texto = recognizer.recognize_google(audio_data, language='pt-BR')
    except sr.UnknownValueError:
        texto = "Não foi possível entender o áudio."
    except sr.RequestError as e:
        texto = f"Erro na solicitação; {e}"

    # Remove o arquivo WAV após a transcrição
    if os.path.exists(wav_path):
        os.remove(wav_path)
        print(' ✅ Arquivo WAV excluído com sucesso! ✅')

    return texto

def enviar_para_openai(texto, tipo='transcricao'):
    """
    Envia o texto para a API da OpenAI para melhorar a transcrição ou gerar um resumo.
    """
    if tipo == 'transcricao':
        prompt = f"Corrija a ortografia, acentuação e pontuação do seguinte texto, mantendo o conteúdo original:\n\n{texto}"
    elif tipo == 'resumo':
        prompt = f"Resuma o seguinte texto de forma clara e concisa, mantendo as informações principais:\n\n{texto}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use o modelo GPT-4
            messages=[{"role": "user", "content": prompt}],
            max_tokens=6000,  # Limite de tokens para a resposta
            temperature=0.7,  # Controla a criatividade da resposta
        )
        resultado = response['choices'][0]['message']['content']
        return resultado
    except openai.error.OpenAIError as e:
        return f"Erro na requisição à OpenAI: {str(e)}"

def processo_completo():
    """
    Função principal que executa o fluxo completo:
    1. Baixa o áudio do YouTube.
    2. Converte o áudio para WAV.
    3. Transcreve o áudio para texto.
    4. Oferece opções para melhorar a transcrição ou gerar um resumo.
    """
    # Baixa o áudio do YouTube
    baixar_mp3_youtube()

    # Encontra o arquivo MP3 baixado no diretório atual
    mp3_path = os.getcwd()  # Usa o diretório atual
    mp3_files = [f for f in os.listdir(mp3_path) if f.endswith('.mp3')]

    if not mp3_files:
        print("❌ Nenhum arquivo MP3 encontrado no diretório. Verifique o caminho e o download.")
        return

    mp3_file = mp3_files[0]
    mp3_full_path = os.path.join(mp3_path, mp3_file)

    # Transcreve o áudio
    texto_transcrito = transcrever_audio(mp3_full_path)
    print('')
    print("✅ Texto transcrito com sucesso ✅")

    while True:
        resposta = input(
            'Você deseja a transcrição do vídeo completa ou um resumo? \n1️⃣ - Transcrição Completa  \n2️⃣ - Resumo \n3️⃣ - Sair do programa: ')

        if resposta == '1':
            print('Aguarde enquanto carregamos a transcrição completa...')
            texto_melhorado = enviar_para_openai(texto_transcrito, tipo='transcricao')
            print(texto_melhorado)

        elif resposta == '2':
            print('Aguarde enquanto carregamos o resumo completo...')
            resumo = enviar_para_openai(texto_transcrito, tipo='resumo')
            print(resumo)

        elif resposta == '3':
            print('Obrigado por usar este programa, até mais <3')
            quit()

        else:
            print('Digite uma opção válida.')

# Executa o processo completo
processo_completo()