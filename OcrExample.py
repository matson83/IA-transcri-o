import whisper
import logging

# Configura o logger para capturar avisos acima do nível ERROR globalmente
logging.basicConfig(level=logging.ERROR)

def transcrever_audio(arquivo_audio):
    try:
        # Carrega o modelo Whisper
        modelo = whisper.load_model("base")

        # Transcreve o áudio e captura a resposta
        resposta = modelo.transcribe(arquivo_audio)

        # Extrai o texto transcrito para melhor legibilidade
        texto_transcrito = resposta.get('text', 'Transcrição não disponível')

        # Insere quebras de linha após pontos, pontos de interrogação e exclamação
        texto_formatado = texto_transcrito.replace('. ', '.\n').replace('? ', '?\n').replace('! ', '!\n')

        # Formata e imprime o texto transcrito com quebras de linha

        print(f"\n\"{texto_formatado}\"\n")
        print("A pesquisa é essa transcrição de um audio político ,  verifique o audio e faça as pesquisas que necessito: ")

        print("\nVerifique se essa informação é uma Fake news :\n")

        print("Mostre as fontes verdadeiras dessa insformação e se possivel o site dessa informação:\n")

    except Exception as e:
        print(f"Ocorreu um erro durante a transcrição: Verifique o tipo do arquivo que foi inserido para a transcrição")

# Define o caminho para o arquivo de áudio e chama a função de transcrição
if __name__ == "__main__":
    arquivo_audio = "gravando2.mp3"
    transcrever_audio(arquivo_audio)




