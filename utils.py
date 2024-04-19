from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

prompt = '''
Kindly get the texts from the image.
'''

your_file = 'lois-1.jpg'
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
response = model.generate_content([prompt, your_file])
print(response.text)