from openai import OpenAI, api_key

client = OpenAI(api_key="sk-proj-G4Y9IDRsW18kej8zMmqxT3BlbkFJdjrzqHl1GpsIcYpMWGq0")


class ChatGPTInteraction:
    def __init__(self, api_key):

    @staticmethod
    def ask_question(question):
        try:
            # headers = {
            #    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
            # }
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": "What color best describes today? Give your answer in the color code and state the reason."}
                ]
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print("Error interacting with ChatGPT:", str(e))
            return None


if __name__ == "__main__":
    chatgpt_interaction = ChatGPTInteraction(api_key)
    response = chatgpt_interaction.ask_question(question)
    if response:
        print("ChatGPT's response:", response)
    else:
        print("Failed to get a response from ChatGPT.")
