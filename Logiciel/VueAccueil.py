# VueAccueil.py
import tkinter as tk
from threading import Thread
from tkinter import ttk, messagebox
from C_Accueil import C_Accueil
from Logiciel.LoadingScreen import LoadingScreen
from Logiciel.VueAnalyse import VueAnalyse
from Logiciel.VueModif import VueModif


class VueAccueil(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mon SEO")
        self.geometry("300x180")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0")
        self.style.configure("TEntry", background="#ffffff")

        self.panel_accueil = ttk.Frame(self, style="TFrame")
        self.panel_accueil.grid(row=0, column=0, padx=20, pady=20)

        self.para=tk.PhotoImage(file="images/para.png").subsample(15,15)
        self.loupe = tk.PhotoImage(file="images/694985.png").subsample(15,15)

        ttk.Label(self.panel_accueil, text="Url:", style="TLabel").grid(row=0, column=0, pady=5, sticky=tk.E)
        ttk.Label(self.panel_accueil, text="Liste mots clés:", style="TLabel").grid(row=1, column=0, pady=5,sticky=tk.E)

        self.txt_url = ttk.Entry(self.panel_accueil, style="TEntry")
        self.txt_mc = ttk.Entry(self.panel_accueil, style="TEntry")
        self.bt_analyser = ttk.Button(self.panel_accueil, image=self.loupe, command=self.analyser)
        self.btn_modifier_parasites = ttk.Button(self.panel_accueil, image=self.para, command=self.ouvrir_vue_modifier_parasites)
        self.txt_url.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        self.txt_mc.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        self.bt_analyser.grid(row=2, column=2, columnspan=2, pady=10)
        self.btn_modifier_parasites.grid(row=2, column=1, columnspan=2, pady=10)

        self.bt_analyser["command"] = self.analyser

        self.c_accueil = C_Accueil()

    def analyser(self):
        url = self.txt_url.get()
        mc_user = self.txt_mc.get().split(',')

        if not url or not mc_user:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        loading_screen = LoadingScreen(self)
        loading_thread = Thread(target=self.analyse_thread, args=(url, mc_user, loading_screen))
        loading_thread.start()

    def analyse_thread (self, url, mc_user, loading_screen):
        try:
            urls_info = self.c_accueil.analyser(url, mc_user)

            vue_analyse = VueAnalyse(self)
            vue_analyse.transient(self)
            vue_analyse.grab_set()
            vue_analyse.configurer_infos(urls_info)
        except Exception as e:
            messagebox.showerror("Erreur lors de l'analyse", f"Une erreur s'est produite : {e}")
        finally:
            self.after(0, loading_screen.hide_loading_screen)

    def ouvrir_vue_modifier_parasites(self):
        vue_modifier_parasites = VueModif(self)
        vue_modifier_parasites.transient(self)
        vue_modifier_parasites.grab_set()
        vue_modifier_parasites.wait_window(vue_modifier_parasites)