from openai import OpenAI
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
client = OpenAI(os.getenv("OPENAI_API_KEY"))
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY env variable must be set")


class ChatGPTInteraction:
    def __init__(self, api_key):
        pass

    @staticmethod
    def ask_question(question):
        try:
            headers = {
                "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
             }
            # response = client.chat.completions.create(
            #    model="gpt-4-turbo",
             #   messages=[
              #      {"role": "system", "content": "You are a creative assistant."},
               #     {"role": "user", "content": "What color best describes today? Give your answer in the color code and state the reason."}
               # ]
           # )
           # return response.choices[0].text.strip()
       # except Exception as e:
        #    print("Error interacting with ChatGPT:", str(e))
         #   return None


if __name__ == "__main__":
    chatgpt_interaction = ChatGPTInteraction(api_key)
    response = chatgpt_interaction.ask_question(question="What color best describes today?")
    if response:
        print("ChatGPT's response:", response)
    else:
        print("Failed to get a response from ChatGPT.")
