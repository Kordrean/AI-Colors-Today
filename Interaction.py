from openai import OpenAI
import os
from dotenv import load_dotenv, dotenv_values
from typing import Optional, Tuple

# load env variables from .env files
load_dotenv()

<<<<<<< HEAD
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

=======
>>>>>>> c54c24d (	modified:   Interaction.py)

# Check if OPENAI_API_KEY s set
if not os.getenv("OPENAI_API_KEY"):
   raise ValueError("OPENAI_API_KEY env variable must be set")

client = OpenAI(os.getenv("OPENAI_API_KEY"))


print(os.getenv("OPENAI_API_KEY"))

print('SUCCESSFULLY CONNECTED TO CLIENT', client)


class ChatGPTInteraction:
    def __init__(self, api_key):
<<<<<<< HEAD
        self.api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def ask_question(self, question_text: str) -> Optional[str]:
=======
        # self.api_key = os.environ.get("OPENAI_API_KEY")
        # openai.api_key = self.api_key
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY env variable must be set")
        self.client = OpenAI(self.api_key)
    @staticmethod
    def ask_question(question_text: str) -> Optional[str]:
>>>>>>> c54c24d (	modified:   Interaction.py)
        try:
            # headers = {
            #     "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
            # }
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user",
                     "content": question_text}
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
