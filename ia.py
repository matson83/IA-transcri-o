import google.generativeai as genai

GOOGLE_API_KEY=('AIzaSyCXlSVeKRo4msWTNdX4sf28HduAwXk1Vjk')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

pergunta = "Quem descobriu o Brasil?"

response = model.generate_content(pergunta)

print(response.text)
