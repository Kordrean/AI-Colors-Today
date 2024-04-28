from gui import ColorGUI
from database import ColorDatabase
from Interaction import ChatGPTInteraction
import os


def main():
    # Initialize GUI
    color_gui = ColorGUI()

    # Initialize Database
    db_file = "color_responses.db"
    color_db = ColorDatabase(db_file)

    # Initialize ChatGPT Interaction
    api_key = os.getenv("OPENAI_API_KEY")
    chatgpt_interaction = ChatGPTInteraction(api_key)

    # Retrieve data from database and update GUI
    responses = color_db.retrieve_responses()

    #List to store color codes and things
    color_codes = []

    for response in responses:
        # print(response)
        color_code = response[0] 
        reason = response[1]

        # display reason on gui
        color_gui.display_color_reason("", reason)

        #Append color code to lsit
        color_codes.append(color_code)
        # print(color_code)

    # Get the current date (needs to implement this functionality)
    current_date = "2024-04-17"  # Placeholder for the current date

    # Ask ChatGPT for the color of the current day
    question = "What color best describes today? Give your answer in the color code and state the reason. Start your reasoning with the phrase '\n\nReason: '. Keep your reasoning within a maximum of 150 characters."
    response = chatgpt_interaction.ask_question(question)

    if response:
        print(response)
        parts = response.split("\n\nReason: ")
        if len(parts) == 2:
            color_code = parts[0].strip()
            reason = parts[1].strip()
            # Store response in database
            color_db.insert_response(current_date, color_code, reason)
            # Update GUI with new response
            color_gui.display_color_reason(current_date, reason)

    # Start GUI event loop
    color_gui.window.mainloop()


if __name__ == "__main__":
    main()
