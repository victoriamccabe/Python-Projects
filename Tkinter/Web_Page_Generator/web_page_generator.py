import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Label for the custom text input
        self.label = Label(self.master, text="Enter Custom Text:")
        self.label.grid(row=0, column=0, padx=10, pady=(10, 0))

        # Frame to hold Text widget and scrollbar side by side
        text_frame = Frame(self.master)
        text_frame.grid(row=1, column=0, padx=(10, 0), pady=(0, 10))

        # Text widget for multi-line input (square-ish)
        self.custom_text = Text(text_frame, width=80, height=4, wrap=WORD)
        self.custom_text.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar widget
        scrollbar = Scrollbar(text_frame, command=self.custom_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Connect scrollbar to Text widget
        self.custom_text.config(yscrollcommand=scrollbar.set)

        # Creates "Default HTML Page" button
        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=0, padx=(0, 250), pady=(0, 10))

        # Creates "Submit Custom Text" button
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=0, padx=(250, 0), pady=(0, 10))

        # Creates "Clear Text" button to clear the Text box
        self.clear_btn = Button(self.master, text="Clear Text", width=10, height=2, command=self.clearText)
        self.clear_btn.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    # This function creates a default HTML document
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        self.createHTMLFile(htmlText)

    # This function creates an HTML document using user input
    def customHTML(self):
        user_text = self.custom_text.get("1.0", END).strip()  # Get all text from the Text widget
        if user_text == "":
            user_text = "You didn't enter any custom text!"   # Fallback message
        self.createHTMLFile(user_text)

    # Helper function to write and open HTML file
    def createHTMLFile(self, text):
        with open("index.html", "w") as htmlFile:
            # Basic HTML structure with user-provided content
            htmlContent = f"<html>\n<body>\n<h1>{text}</h1>\n</body>\n</html>"
            htmlFile.write(htmlContent)
        webbrowser.open_new_tab("index.html")  # Opens the file in a new browser tab

    # This function clears the Text widget
    def clearText(self):
        self.custom_text.delete("1.0", END)


# Entry point for the application
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


