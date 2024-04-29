import tkinter as tk
from database import ColorDatabase


class ColorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Daily Color Analysis")
        self.window.geometry("800x600")
        self.database = ColorDatabase("color_responses.db")

        # self.response_label = tk.Label(self.window, text="", wraplength=600)
        # self.response_label.pack(side=tk.TOP, fill=tk.X)
        responses = self.database.retrieve_responses()
        print(responses)
        if responses:
            latest_response = responses[-1] # Assuming the latest response is at the end of the list
            color_code, _ = latest_response #Unpack date, color_code, and reason
            button_text = f"Color Code: {color_code}" # Display the color code on the button
        else:
            button_text = "Click Me" # Display the default text on the button for if response doesn't work
    
        self.button = tk.Button(self.window, text=f"{button_text}", command=self.button_click)
        self.button.pack()

        self.reason_label = None # Placeholder for the new label


        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack()




    # def create_gradient(self):
        # clear canvas
        # self.canvas.delete("all")

        # draw rainbow gradient
        # for i in range(256):
            # color = f"#{i:02X}00FF"
            # self.canvas.create_rectangle(0, i * 400 / 255, 600, (i + 1) * 400 / 255, fill=color, outline="")
    
    # def display_color_reason(self, date, color_code):
        # Display reason for selected date
        # self.window.title(f"Color Analysis - {date}")
        # self.response_label.config(text=f"Color Code: {color_code}")

    
    def update_gui(self):
        # Retrieve data from the database
        responses = self.database.retrieve_responses()

        # Clear canvas
        self.canvas.delete("all")

        # Draw rainbow gradient
        # self.create_gradient()

        # Display latest reason in the label
        if responses:
            latest_response = responses[-1] #Assuming the latest response is at the end of the list
            if len(latest_response) == 3:
                _, _, reason = latest_response
                if not self.reason_label:
                    self.reason_label = tk.Label(self.window, text=f"Reason: {reason}", wraplength=550)
                    self.reason_label.pack(side=tk.TOP)
                else:
                    self.reason_label.config(text=f"Reason: {reason}")

    def button_click(self):
        # Define the behavior when the button is clicked
        # print("BUtton clicked")
        if not self.reason_label:
            self.reason_label = tk.Label(self.window, text="Reason: ", wraplength=550)
            self.reason_label.pack(side=tk.TOP)
        
        # Retrieve the latest reason from the database for the button click
        responses = self.database.retrieve_responses()
        if responses:
            latest_response = responses[-1]  # Assuming the latest response is at the end of the list
            if len(latest_response) == 2:
                _, reason = latest_response
                # Update the text of the new label with the latest reason
                self.reason_label.config(text=f"Reason: {reason}")
            elif len(latest_response) == 3:
                _, _, reason = latest_response
                # Update the text of the new label with the latest reason
                self.reason_label.config(text=f"Reason: {reason}")

if __name__ == "__main__":
    color_gui = ColorGUI()
    color_gui.create_gradient()
    color_gui.update_gui()
    color_gui.window.mainloop()
