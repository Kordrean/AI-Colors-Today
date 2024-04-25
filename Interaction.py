import openai
import requests


class ChatGPTInteraction:
    def __init__(self, api_key):
        openai.api_key = api_key

        api_key = "sk-proj-G4Y9IDRsW18kej8zMmqxT3BlbkFJdjrzqHl1GpsIcYpMWGq0"
    def ask_question(self, question):
        try:
            headers = {
                "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
            }
            response = requests.post(
                endpoint_url,
                headers=headers
                engine="text-davinci-002",
                prompt=question,
                max_tokens=50
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print("Error interacting with ChatGPT:", str(e))
            return None

# Example usage:
if __name__ == "__main__":
    api_key = "YOUR_OPENAI_API_KEY"
    chatgpt_interaction = ChatGPTInteraction(api_key)
    question = "What color best describes today? Give your answer in the color code and state the reason."
    response = chatgpt_interaction.ask_question(question)
    if response:
        print("ChatGPT's response:", response)
    else:
        print("Failed to get a response from ChatGPT.")
