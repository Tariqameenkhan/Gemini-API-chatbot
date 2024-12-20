
# chatbot
!pip install google-generativeai
!pip install -q -U google-generativeai

# method 1
import google.generativeai as genai
from google.colab import userdata
GEMINI_API_KEY = userdata.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

user_input_history = []

while True:
    user_input = input("How can i help you ? : ")
    if user_input.lower() == "exit":
        break
    print("Generating response...")
    response = model.generate_content(user_input)
    print(response.text)
    user_input_history.append({"user": user_input, "response": response.text})
user_input_history

# chatbot Method 2
import google.generativeai as genai
from google.colab import userdata


GEMINI_API_KEY = userdata.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

user_input_history = []

while True:
    user_input = input("How can I help you? : ")
    if user_input.lower() == "exit":
        break

    print("Generating response...")
    try:
        response = model.generate_content(user_input)
        print(response.text)
        user_input_history.append({"user": user_input, "response": response.text})
    except Exception as e:
        print(f"An error occurred: {e}")

user_input_history