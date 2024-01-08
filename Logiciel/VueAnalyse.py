import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class VueAnalyse(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.urls_info = []
        self.taille_page = 3
        self.page_actuelle = 0

        self.title("Analyse des URLs")
        self.geometry("800x600")

        self.panel_analyse = ttk.Frame(self, padding=(10, 10))
        self.panel_analyse.pack(expand=True, fill="both")

        tk.Label(self.panel_analyse, text="Analyse des URLs", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        self.listbox = tk.Listbox(self.panel_analyse, width=100, height=20)
        self.listbox.grid(row=1, column=0, columnspan=2, pady=10)

        self.btn_precedent = tk.Button(self.panel_analyse, text="Précédent", command=self.page_precedente)
        self.btn_precedent.grid(row=2, column=0, pady=10, sticky=tk.W)

        self.btn_suivant = tk.Button(self.panel_analyse, text="Suivant", command=self.page_suivante)
        self.btn_suivant.grid(row=2, column=1, pady=10, sticky=tk.W)

        self.btn_sauvegarder = tk.Button(self.panel_analyse, text="sauvegarder", command=self.sauvegarder_rapport)
        self.btn_sauvegarder.grid(row=3, column=0, pady=10, sticky=tk.W)

    def configurer_infos(self, urls_info):
        self.urls_info = urls_info
        self.afficher_page_resultats()

    def afficher_page_resultats(self):
        self.listbox.delete(0, tk.END)

        debut = self.page_actuelle * self.taille_page
        fin = debut + self.taille_page
        page_urls_info = self.urls_info[debut:fin]

        for url_info in page_urls_info:
            self.afficher_info_url(url_info)

    def page_suivante(self):
        if (self.page_actuelle + 1) * self.taille_page < len(self.urls_info):
            self.page_actuelle += 1
            self.afficher_page_resultats()

    def page_precedente(self):
        if self.page_actuelle > 0:
            self.page_actuelle -= 1
            self.afficher_page_resultats()

    def afficher_info_url(self, url_info):
        self.listbox.insert(tk.END, f"URL: {url_info['url']}")
        self.listbox.insert(tk.END, f"Liens sortants: {url_info['liens_sortants']}")
        self.listbox.insert(tk.END, f"Liens internes: {url_info['liens_internes']}")
        self.listbox.insert(tk.END, f"% Balises alt: {url_info['pourcentage_balises_alt']}")
        self.listbox.insert(tk.END, f"Mots clés pertinents: {', '.join(url_info['mots_cles_pertinents'][:3])}")

        mc_user_present = any(mcu in url_info['mots_cles_pertinents'][:3] for mcu in url_info.get('mots_cles_utilisateur', []))
        self.listbox.insert(tk.END, f"Mots clés utilisateur présents: {'Oui' if mc_user_present else 'Non'}")

        self.listbox.insert(tk.END, "")

    def sauvegarder_rapport(self):
        try:
            fichier_destination = filedialog.asksaveasfilename(defaultextension=".json",filetypes=[("Fichiers JSON", "*.json")])

            if fichier_destination:

                rapport = []

                for url_info in self.urls_info:
                    mc_user_present = any(mcu in url_info['mots_cles_pertinents'][:3] for mcu in
                                          url_info.get('mots_cles_utilisateur', []))
                    rapport.append({
                        "URL": url_info['url'],
                        "Liens sortants": url_info['liens_sortants'],
                        "Liens internes": url_info['liens_internes'],
                        "% Balises alt": url_info['pourcentage_balises_alt'],
                        "Mots clés pertinents": url_info['mots_cles_pertinents'][:3],
                        "Mots clés utilisateur présents": 'Oui' if mc_user_present else 'Non'
                    })


                with open(fichier_destination, 'w') as fichier_json:
                    json.dump(rapport, fichier_json, indent=2)

                messagebox.showinfo("Sauvegarde réussie", "Le rapport a été sauvegardé.")

        except Exception as e:
            messagebox.showerror("Erreur lors de la sauvegarde", f"Une erreur s'est produite : {e}")
