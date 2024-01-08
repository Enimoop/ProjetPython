# MonSeo.py
import tkinter as tk
from VueAccueil import VueAccueil

class MonSeo:
    def __init__(self):
        self.vue_accueil = VueAccueil()
        self.vue_analyse = None


if __name__ == "__main__":
    try:
        mon_seo_app = MonSeo()
        mon_seo_app.vue_accueil.mainloop()
    except Exception as e:
        print(f"Erreur : {e}")
