import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class VueModif(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Modifier Parasites")
        self.geometry("800x700")

        self.label_instructions = ttk.Label(self, text="Modifiez la liste des parasites :")
        self.label_instructions.pack(pady=10)

        self.liste_parasites = tk.Listbox(self, selectmode=tk.MULTIPLE, height=25, width=50)
        self.liste_parasites.pack(pady=10)

        self.charger_liste_existante()

        self.label_nouveaux_parasites = ttk.Label(self,text="Ajouter de nouveaux parasites:")
        self.label_nouveaux_parasites.pack(pady=5)

        self.txt_parasite = ttk.Entry(self)
        self.txt_parasite.pack(pady=10)

        self.btn_enregistrer = ttk.Button(self, text="Enregistrer", command=self.enregistrer_parasite)
        self.btn_enregistrer.pack(pady=10)

        self.btn_supprimer = ttk.Button(self, text="Supprimer", command=self.supprimer_parasite)
        self.btn_supprimer.pack(pady=10)

    def charger_liste_existante(self):
        try:
            with open('parasite.csv', 'r') as fichier:
                parasites_existants = fichier.read().split('\n')
                for parasite in parasites_existants:
                    self.liste_parasites.insert(tk.END, parasite)

        except FileNotFoundError:
            pass

    def enregistrer_parasite(self):
        nouveau_parasite = self.txt_parasite.get()

        if nouveau_parasite:
            try:
                with open('parasite.csv', 'a') as fichier:
                    fichier.write(f"{nouveau_parasite}\n")

                self.liste_parasites.insert(tk.END, nouveau_parasite)

                messagebox.showinfo("Ajouté", "Nouveau parasite ajouté.")

                self.txt_parasite.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement : {e}")
        else:
            messagebox.showwarning("Attention", "Veuillez entrer un parasite avant d'ajouter.")

    def supprimer_parasite(self):
        selection = self.liste_parasites.curselection()

        if not selection:
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner au moins un parasite à supprimer.")
            return

        confirm = messagebox.askyesno("Confirmer la suppression", "Voulez-vous vraiment supprimer les parasites sélectionnés?")

        if confirm:
            parasites_a_supprimer = [self.liste_parasites.get(index) for index in selection]

            with open('parasite.csv', 'r') as fichier:
                parasites_existants = fichier.read().split('\n')

            with open('parasite.csv', 'w') as fichier:
                for parasite in parasites_existants:
                    if parasite not in parasites_a_supprimer:
                        fichier.write(f"{parasite}\n")

            self.liste_parasites.delete(0, tk.END)
            self.charger_liste_existante()

            messagebox.showinfo("Supprimé", "Parasites supprimés avec succès.")