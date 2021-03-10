import os.path
import pickle

from conui import Contact

_path_ = "data.dat"


def load() -> dict:
    if os.path.exists(_path_):
        with open(_path_, "rb") as file:
            data = pickle.load(file)
        return data
    else:
        return {}


def save(db:dict):
    with open(_path_, "wb") as file:
        pickle.dump(db, file, pickle.HIGHEST_PROTOCOL)


def create(db:dict,contact: Contact):
    db[get_code(contact)] = contact


def read(db:dict,id: str) -> Contact:
    return db[id]


def update(db:dict, old: Contact, new: Contact):
    db[get_code(old)] = new


def get_code(contact: Contact) -> str:
    return contact.f_name[:3] + contact.l_name[:3]


def delete(db:dict, contact: Contact):
    del db[get_code(contact)]


def exists(db:dict, contact: Contact) -> bool:
    return get_code(contact) in db


def search(db: dict, name: str) -> list[[Contact]]:
    rslt = []
    for contact in db.values():
        if contact.l_name.lower().startswith(name):
            rslt.append(contact)
    return rslt


def findall(db:dict):
    return list(db.values())


def find(contact: Contact) -> Contact:
    return read(get_code(contact))
