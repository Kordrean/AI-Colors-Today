from openai import OpenAI
import os
from dotenv import load_dotenv, dotenv_values
from typing import Optional, Tuple

# load env variables from .env files
load_dotenv()


# Check if OPENAI_API_KEY s set
if not os.getenv("OPENAI_API_KEY"):
   raise ValueError("OPENAI_API_KEY env variable must be set")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Check if the client is connected
# print('SUCCESSFULLY CONNECTED TO CLIENT', client)


class ChatGPTInteraction:
    def __init__(self, api_key):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY env variable must be set")
        self.client = OpenAI(api_key=self.api_key)
    @staticmethod
    def ask_question(question_text: str) -> Optional[str]:
        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative assistant who gives unique responses."},
                    {"role": "user",
                     "content": question_text},
                    {"role": "system", "content": "", "temperature": 1.2} #Higher temperature means more randomness
                ]
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print("Error interacting with ChatGPT:", str(e))
            return None

    def extract_color_and_reason(response: str) -> Tuple[Optional[str], Optional[str]]:
        # Assuming response is in the format: "color_code: reason"
        parts = response.split("\n\nReason: ")
        if len(parts) == 2:
            color_code = parts[0].strip()
            reason = parts[1].strip()
            return color_code, reason
        else:
            return None, None


if __name__ == "__main__":
    chatgpt_interaction = ChatGPTInteraction(api_key=os.getenv("OPENAI_API_KEY"))
    question = "What color best describes today? Give your answer in the color code and state the reason why."
    response_text = chatgpt_interaction.ask_question(question)
    if response_text:
        print("ChatGPT's response:", response_text)
    else:
        print("Failed to get a response from ChatGPT.")
