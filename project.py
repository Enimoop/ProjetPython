from collections import Counter
import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def etape1(text):
    l=text.split(' ')
    dic = {}
    for j in l:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    dicfinal={key:value for key, value in sorted(dic.items(), key=lambda item:item[1], reverse=True)}
    return dicfinal





def etape2(occ, parasites):
    occ_filtre = {word: count for word, count in occ.items() if word.lower() not in set(parasites)}
    occ_clean = {word: count for word, count in occ_filtre.items() if word and word.strip()}
    return occ_clean






def etape3 (fichier):
    dic = []
    with open(fichier, "r") as file:
        reader = csv.reader(file,delimiter='\n')
        for ligne in reader:
            dic += ligne
    return dic



def etape5(html):
    soup = BeautifulSoup(html,"html.parser")
    sans_html = soup.get_text(separator=" ")
    return sans_html




def etape6(chaine,balise,attribut):
    liste = []
    soup = BeautifulSoup(chaine, 'html.parser')
    balise_list = soup.find_all(balise)
    for element in balise_list:
        liste.append(element[attribut])
    return liste




def etape8(url):
    url_parts = urlparse(url)
    domaine = url_parts.netloc
    return domaine




def etape9(domaine,liste_url):
    yes_list = []
    no_list = []
    for url in liste_url:
        if etape8(url)==domaine:
            yes_list.append(url)
        else:
            no_list.append(url)
    return {'domain_url': yes_list,'not_domain_url': no_list}



def etape10(url):
    response=requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        html_text = soup.prettify()
        return html_text
    else:
        print(f"Erreur de requête HTTP : {response.status_code}")




