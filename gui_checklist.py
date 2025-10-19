import tkinter as tk

class ChecklistApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Checklist")
        self.root.geometry("250x375")
        self.root.resizable(False, False)

    def run(self):
        self.root.mainloop()
