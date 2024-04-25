import tkinter as tk
from database import ColorDatabase


class ColorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Daily Color Analysis")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.database = ColorDatabase("color_responses.db")

    def create_gradient(self):
        #clear canvas
        self.canvas.delete("all")

        #draw rainbow gradient
        for i in range(256):
            color = f"#{i:02X}00FF"
            self.canvas.create_rectangle(0, i * 400 / 255, 600, (i + 1) * 400 / 255, fill=color, outline="")
    
    def display_color_reason(self, date, reason):
        # Display reason for selected date
        self.root.title(f"Color Analysis - {date}")
        self.status_bar.config(text=reason)

    def update_gui(self):
        # Retrieve data from the database
        responses = self.database.retrieve_responses()

        # Clear canvas
        self.canvas.delete("all")

        # Draw rainbow gradient
        self.create_gradient()

        # Display reasons for each date
        for response in responses:
            date, color_code, reason = response
            self.display_color_reason(date, reason)


if __name__ == "__main__":
    color_gui = ColorGUI()
    color_gui.create_gradient()
    color_gui.update_gui()
    color_gui.root.mainloop()
