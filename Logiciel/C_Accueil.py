# C_Accueil.py
import csv
from urllib.parse import urlparse

from C_Analyse import C_Analyse
from Logiciel.VueAnalyse import VueAnalyse
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

class C_Accueil:
    def __init__(self):
        self.analyseur = C_Analyse()

    def analyser(self, url, mc_user):

        domaine = self.analyseur.etape8(url)

        urls_principales = self.analyseur.etape6(self.analyseur.etape10(url), 'a', 'href',domaine)

        print("Liens récupérés :", urls_principales)

        urls_info = []

        for url_page in urls_principales:
            if not url_page.startswith(('http:', 'https:')):
                continue

            print("Analyse de la page :", url_page)

            html_content = self.analyseur.etape10(url_page)

            if html_content is not None:
                text_without_html = self.analyseur.etape5(html_content)

                words_occ = self.analyseur.etape1(text_without_html)

                parasites = self.analyseur.etape3('parasite.csv')

                clean_words_occ = self.analyseur.etape2(words_occ, parasites)

                img_alt_values = self.analyseur.etape6(html_content, 'img', 'alt', domaine)

                pourcentage = self.analyseur.pourcentage_bal(img_alt_values)

                href_values = self.analyseur.etape6(html_content, 'a', 'href', domaine)

                urls_in_domain, urls_not_in_domain = self.analyseur.etape9(domaine, href_values)

                urls_info.append(
                    {
                        "url": url_page,
                        "liens_sortants": len(urls_not_in_domain),
                        "liens_internes": len(urls_in_domain),
                        "pourcentage_balises_alt": pourcentage,
                        "mots_cles_pertinents": list(clean_words_occ.keys()),
                        "mots_cles_utilisateur": mc_user,
                    })

        return urls_info
