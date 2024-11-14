import sys
from pydub import AudioSegment
import numpy as np
import librosa
import soundfile as sf
from pydub import AudioSegment

def remove_vocals(input_file):
    try:
        # Carregar o arquivo de áudio MP3 usando librosa
        y, sr = librosa.load(input_file, sr=None, mono=False)

        # Verifica se o áudio é estéreo
        if y.shape[0] != 2:
            print("O arquivo de áudio não é estéreo. Esta técnica funciona apenas com arquivos estéreo.")
            return

        # Separação de canais (esquerdo e direito)
        left, right = y

        # Subtração de canais para remover o vocal
        instrumental = left - right

        # Salvar o áudio instrumental temporariamente como WAV
        temp_wav = "temp_instrumental.wav"
        sf.write(temp_wav, instrumental, sr)

        # Converter o arquivo WAV para MP3 usando pydub
        instrumental_audio = AudioSegment.from_wav(temp_wav)
        output_file = input_file.rsplit('.', 1)[0] + '_instrumental.mp3'
        instrumental_audio.export(output_file, format="mp3")
        print(f"Vocal removido e arquivo salvo como: {output_file}")

    except Exception as e:
        print(f"Erro ao processar o áudio: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python remove_vocal.py <nome do arquivo .mp3>")
    else:
        audio_file = sys.argv[1]
        remove_vocals(audio_file)
