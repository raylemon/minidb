"""
Ne modifiez pas ce fichier.
"""

from collections import namedtuple

import sqlite as db

Contact = namedtuple("Contact", ["f_name", "l_name", "tel"])  # Création d’un tuple nommé similaire à une classe
data = None


def i_menu() -> str:
    """
    Menu interactif
    Permet à l’utilisateur de choisir une des fonctions du menu
    :returns une lettre valide parmi les lettres suivantes : A C S R E Q V M
    """
    choice = "."
    while choice not in "ACSREQVM":
        print(
            "[V]oir les contacts" +
            "\n[A]jouter un contact" +
            "\n[E]nlever un contact" +
            "\n[R]echercher un contact" +
            "\n[M]odifier un contact"
            "\n[S]auver les contacts" +
            "\n[C]harger les contacs" +
            "\n[Q]uitter le programme"
        )
        choice = input("Votre choix: ").upper()
    return choice


def question(prompt: str) -> bool:
    """
    Permet de poser une question et de s’assurer que le résultat soit bien [O]ui ou [N]on
    :param prompt: la question à poser.
    :return: True si la demande a été validée (O), False sinon (N)
    """
    x = input(prompt + " [o/N]").upper() or "N"
    while x not in "ON":
        x = input("Répondez par [O]ui ou [N]on svp: ").upper()
    return x == "O"


def i_add():
    """
    Ajout d’un contact de façon interactive
    Demande le nom, prénom et n° de téléphone d’un contact.
    Vérifie la validité du n° de téléphone
    Ajoute le contact dans la base de donnée.
    """
    l_name = input("Entrez le nom de votre contact: ")
    f_name = input("Entrez le prénom de votre contact: ")
    tel = input("Entrez le n° de téléphone de votre contact: ")

    contact = Contact(f_name, l_name, tel)

    if not verif(tel):
        tel = input("N° incorrect. Vérifiez et retapez le code: ")

    if db.exists(data, contact):
        print("Attention ! Le contact existe déjà ! Appuyez sur 'M' pour modifier un contact depuis le menu")
    else:
        if not question(f"Ce contact sera créé: {f_name} {l_name} ({tel}). Est-correct ?"):
            print("Abandon")
        else:
            db.create(data, contact)


def i_view():
    """
    Affiche tous les contacts de la base de données
    """
    print("-" * 80)
    contacts = db.findall(data)
    for contact in contacts:
        i_print_contact(contact)
        print("-" * 80)


def i_search():
    """
    Recherche les contacts selon leur nom de famille
    """
    part_name = input("Tapez le début du nom à rechercher: ").lower()
    lst = db.search(data, part_name)
    if len(lst) != 0:
        for contact in lst:
            i_print_contact(contact)
    else:
        print("Pas d’occurrence trouvée")


def i_print_contact(contact: Contact):
    """
    Affiche le contact sélectionné
    :param contact: un Contact
    """
    print("Nom: ", contact.l_name)
    print("Prénom:", contact.f_name)
    print("Tel:", contact.tel)


def i_delete():
    """
    Sélectionne un contact pour suppression dans la db
    """
    part_name = input("Tapez le début du nom à supprimer: ").lower()
    lst = db.search(data, part_name)
    if len(lst) != 0:
        for contact in lst:
            i_print_contact(contact)
            if question("Voulez-vous supprimer ce contact ?"):
                db.delete(data, contact)
    else:
        print("Pas d’occurrence trouvée")


def i_update():
    """
    Sélectionne un contact pour mise à jour
    """
    part_name = input("Tapez le début du nom à modifier: ").lower()
    lst = db.search(data, part_name)
    if len(lst) != 0:
        for old_contact in lst:
            i_print_contact(old_contact)
            if question("Voulez-vous modifier ce contact ?"):
                new_l_name = input(
                    "Entrez le nouveau nom du contact ou laissez vide pour conserver: ") or old_contact.l_name
                new_f_name = input(
                    "Entrez le nouveau prénom du contact ou laissez vide pour conserver: ") or old_contact.f_name
                new_tel = input(
                    "Entrez le nouveau n° de téléphone du contact ou laissez vide pour conserver: ") or old_contact.tel
                while not verif(new_tel):
                    new_tel = input("N° incorrect. Vérifiez et retapez le code: ")
                new_contact = Contact(new_f_name, new_l_name, new_tel)
                db.update(data, old_contact, new_contact)


def verif(tel: str) -> bool:
    """
    Vérifie la validité d’un n° de téléphone. Peut être amélioré avec les expressions rationnelles
    :param tel: un numéro de téléphone
    :return: True si le numéro est valide, False sinon
    """
    tel = clean(tel)
    return 9 <= len(tel) <= 10


def clean(tel: str) -> str:
    """
    Nettoie un numéro de téléphone pour supprimer tous les caractères non numériques
    :param tel: le texte à nettoyer
    :return: le texte nettoyé
    """
    rep = ""
    for letter in tel:
        if letter.isdigit():
            rep += letter
    return rep


if __name__ == '__main__':
    data = db.load()
    print("Chargement des données effectué")
    saved = False
    m = ""
    while m != "Q":
        m = i_menu()

        if m == "A":
            i_add()
        elif m == "S":
            db.save(data)
        elif m == "R":
            i_search()
        elif m == "E":
            i_delete()
        elif m == "Q":
            if not saved:
                print("Sauvegarde...")
                db.save(data)
                saved = not saved

        elif m == "C":
            if not saved:
                db.save(data)
            data = db.load()
            print("Chargement des données effectué")

        elif m == "V":
            i_view()

        elif m == "M":
            i_update()
