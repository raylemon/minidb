from conui import Contact

""" La base de données doit être un dictionnaire de contacts. La clé unique de chaque contact est constituée des
    trois premières lettres du nom de famille suivi des trois premières lettres du prénom.
    
    Pour ceux qui sont tentés de faire une base de données à la place... Ça sera le sujet du prochain cours !
"""


def exists(db:dict, contact:Contact) -> bool:
    """
    Vérifie si un contact existe dans le dictionnaire
    :param contact: le contact à vérifier
    :return: True si le contact existe, False sinon
    """
    pass


def create(db:dict, contact:Contact):
    """
    Ajoute un contact dans le dictionnaire
    :param contact: le contact à ajouter
    """
    pass


def findall(db:dict) -> list[[Contact]]:
    """
    Génère une liste de contacts depuis le dictionnaire
    :return: une liste de Contact
    """
    pass


def search(db:dict, filter:str) -> list[[Contact]]:
    """
    Génère une liste de contacts correspondants au filtre de recherche
    :param filter: le début du nom à rechercher
    :return: une liste de Contact correspondants au critère de recherche
    """
    pass


def delete(db:dict,contact:Contact):
    """
    Supprime un contact du dictionnaire
    :param contact: le contact à supprimer
    """
    pass


def load() -> dict:
    """
    Charge le fichier 'data.dat' en mémoire. Le fichier sera enregistré avec le module pickle (stockez le dictionnaire
    au complet avec pickle)
    Si le fichier n’existe pas, on crée un dictionnaire en mémoire. S’il existe, on charge le dictionnaire en mémoire.
    :return: True si le fichier existe et est chargé, False sinon
    """
    pass



def save(db:dict):
    """
    Enregistre le dictionnaire dans un fichier sous le nom 'data.dat'
    """
    pass


def update(db:dict, old_contact:Contact, new_contact:Contact):
    """
    Met à jour un contact dans le dictionnaire
    :param old_contact: L’ancien contact à remplacer
    :param new_contact: Le nouveau contact
    """
    pass

def read(db:dict, id:str) -> Contact:
    """
    Lit un contact du dictionnaire depuis son identifiant
    :param id: L’identifiant (unique) du contact
    :return: Le contact
    """

def get_code(contact:Contact)->str:
    """
    Génère un code pour le contact. Le code est constitué des 3 premières lettres du nom suivi des 3 premières lettres
    du prénom
    :param contact: le contact à coder
    :return: la clé (unique?) du contact
    """
