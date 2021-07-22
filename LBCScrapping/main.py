# Code from Thomas Deleforge
import requests as req
from bs4 import BeautifulSoup
import requests

try:
    # 200: Ok
    # 403: Forbidden
    # 203: No content
    # 404: Error
    # global variable
    website = "https://www.leboncoin.fr/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/91.0.4472.164 Safari/537.36'}

    # request to get web content
    req = requests.get(website, headers=headers)
    website_details = req.content.decode()

    # beautifulsoup
    soup = BeautifulSoup(website_details, "html.parser")
    print("soup : ", soup)

    print("website : ", website)
    print("req : ", req)

    # dictionary and variable that constitute the url
    # link = website+'/recherche?'+category=''&locations=''&real_estate_type=''&price=''&square=''
    category = 9 # "Ventes immobilières"
    city_dict = {
        "La Madeleine": "La%20Madeleine_59110__50.65507_3.07373_1503",
        "Marcq en Baroeul": "Marcq-en-Baroeul_59700__50.674_3.0942_4350",
        "Lomme": "Lomme_59160__50.63904_3.01242_6000",
        "Saint Andre": "Saint-André-lez-Lille_59350__50.66137_3.05029_2406",
        "Lambersart": "Lambersart_59130__50.64782_3.02267_2745",
        "Pellevoisin": "Saint-Maurice-Pellevoisin_59800",
        "Hellesme": "Hellemmes-Lille_59260__50.62729_3.10866_6000",
        "Croix": "Croix_59170__50.6798_3.15686_2530"
    }
    type_bien_dict = {
        "Maison": 1,
        "Appartement": 2,
        "Autres": 5
    }
    price_min, price_max = 'min', 'max'
    square_min, square_max = 'min', 'max'

    # Request to have page with all parameters on
    price_max = 300000
    square_min = 80
    final_page = 'https://www.leboncoin.fr/recherche?category=9&locations=La%20Madeleine_59110__50.65507_3.07373_1503&price=min-325000&square=80-max'
        #f"{website}recherche?category={category}&locations={city_dict[0]}" \
        #         f"&real_estate_type={type_bien_dict[0]}&price={price_min}-{price_max}&square={square_min}-{square_max}"

    print("je suis ici : ", final_page)
    # request to get web content
    req2 = requests.get(final_page, headers=headers)
    website_details2 = req2.content.decode()

    # beautifulsoup
    soup2 = BeautifulSoup(website_details2, "html.parser")
    print("soup : ", soup2)

    print("website : ", final_page)
    print("req : ", req2)


# la madeleine
# https://www.leboncoin.fr/recherche?category=9&locations=La%20Madeleine_59110__50.65507_3.07373_1503&real_estate_type=1&price=min-325000&square=80-max

# marcq en baroeul
# https://www.leboncoin.fr/recherche?category=9&locations=Marcq-en-Baroeul_59700__50.674_3.0942_4350&real_estate_type=1&price=min-325000&square=80-max

except:
    print("Error loading page...")


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Code Structure
# """
# Entrer les paramètres d'entrée : ville, type, prix, surface
#     Charger le résultat
#         Si plusieurs pages, alors on boucle sur le nb de page
#         Sinon, sur la seule page dispo
#             Afficher la liste des informations : lieu, prix, superficie, prix/mcarré, lien web pour accéder à la page
#             enregistrer chaque ligne dans un tableau sous excel pour faciliter l'utilisation
#
# Par la suite, faire une GUI pour que ce soit simple d'utilisation pour Aude
# """
