import google.generativeai as genai
import whisper

model = whisper.load_model("tiny")
audio_path = "C:/Users/matso/Documents/OCR/OCR/gravando2.mp3"

API_KEY = 'AIzaSyCGW81sQiyNEp5ZjkreCU5l0rijOTBexAE'
genai.configure(api_key=API_KEY)


def pergunta():
    result = model.transcribe(audio_path)
    transcript = result["text"]

    modelo = genai.GenerativeModel('gemini-pro')
    pergunta = ('qual o tema desta fala? \n'
                'Mostre as fontes : \n'
                'Mostre quem é citado nessa fala :')
    transcricao = pergunta + "\n" + transcript
    resposta = modelo.generate_content(transcricao)

    print(f"Resposta: \n{resposta.text}")
    print("Transcrição: \n{}".format(transcript.replace('. ', '.\n').replace('? ', '?\n').replace('! ', '!\n')))


pergunta()