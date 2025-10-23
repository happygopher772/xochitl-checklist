import tkinter as tk
from main_window import MainWindow

class ChecklistApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Xochitl Checklist")
        self.root.geometry("300x375")
        self.root.resizable(True, True)

        self.photo = tk.PhotoImage(file='xochitl_logo.png')
        self.root.iconphoto(False, self.photo)

        self.main_window = MainWindow(self.root)

    def run(self):
        self.root.mainloop()
