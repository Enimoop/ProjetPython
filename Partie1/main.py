from project import *
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def main():
    url = input("Entrez l'URL de la page à analyser : ")

    html_content = etape10(url)

    text_without_html = etape5(html_content)

    words_occ = etape1(text_without_html)

    parasites = etape3('parasite.csv')

    clean_words_occ = etape2(words_occ, parasites)

    img_alt_values = etape6(html_content, 'img', 'alt')

    href_values = etape6(html_content, 'a', 'href')

    domaine = etape8(url)

    urls_in_domain, urls_not_in_domain = etape9(domaine, href_values)

    print("Mots clés avec occurrences :")
    print(dict(list(clean_words_occ.items())[:3]))

    print("\nNombre de liens entrants :", len(urls_in_domain))
    print("Nombre de liens sortants :", len(urls_not_in_domain))

    print("\nBalises alt des images :")
    print(img_alt_values)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
