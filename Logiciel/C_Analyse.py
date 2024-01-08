# C_Analyse.py
from urllib.parse import urljoin, urlparse
import csv
import requests
from bs4 import BeautifulSoup

class C_Analyse:
    @staticmethod
    def etape1(text):
        l = text.split(' ')
        dic = {}
        for j in l:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        dicfinal = {key: value for key, value in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        return dicfinal

    @staticmethod
    def etape2(occ, parasites):
        occ_filtre = {word: count for word, count in occ.items() if word.lower() not in set(parasites)}
        occ_clean = {word: count for word, count in occ_filtre.items() if word and word.strip()}
        return occ_clean

    @staticmethod
    def etape3(fichier):
        dic = []
        with open(fichier, "r") as file:
            reader = csv.reader(file, delimiter='\n')
            for ligne in reader:
                dic += ligne
        return dic

    @staticmethod
    def etape5(html):
        soup = BeautifulSoup(html, "html.parser")
        sans_html = soup.get_text(separator=" ")
        return sans_html

    @staticmethod
    def etape6(chaine, balise, attribut, url_base):
        liste = []
        soup = BeautifulSoup(chaine, 'html.parser')
        balise_list = soup.find_all(balise)

        for element in balise_list:
            if attribut in element.attrs:
                lien = element[attribut]

                if lien.startswith(('http:', 'https:')):
                    liste.append(lien)
                else:
                    absolu = urljoin("https://" + url_base, lien)
                    liste.append(absolu)
        return liste

    @staticmethod
    def etape8(url):
        url_parts = urlparse(url)
        domaine = url_parts.netloc
        return domaine

    @staticmethod
    def etape9(domaine, liste_url):
        yes_list = []
        no_list = []
        for url in liste_url:
            if C_Analyse.etape8(url) == domaine:
                yes_list.append(url)
            else:
                no_list.append(url)
        return yes_list, no_list

    @staticmethod
    def etape10(url):
        try:
            print(f"Tentative de requête HTTP pour l'URL : {url}")
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                html_text = soup.prettify()
                return html_text
            else:
                print(f"Erreur de requête HTTP : {response.status_code}")
                return None
        except Exception as e:
            print(f"Erreur lors de la requête HTTP : {e}")
            return None

    @staticmethod
    def pourcentage_bal(img_alt_value):
        all_images = len(img_alt_value)
        images_with_alt = sum(1 for alt_value in img_alt_value if alt_value)

        if all_images > 0:
            pourcentage_balises_alt = (images_with_alt / all_images) * 100
        else:
            pourcentage_balises_alt = 0

        return pourcentage_balises_alt
