import tkinter as tk
from tkinter import ttk


class LoadingScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Chargement en cours...")
        self.geometry("300x100")

        self.label = ttk.Label(self, text="Analyse en cours...")
        self.label.pack(pady=20)

        self.progress_bar = ttk.Progressbar(self, mode="indeterminate")
        self.progress_bar.pack()

        self.protocol("WM_DELETE_WINDOW", self.hide_loading_screen)

    def show_loading_screen(self):
        self.deiconify()
        self.progress_bar.start()

    def hide_loading_screen(self):
        self.withdraw()
        self.progress_bar.stop()
