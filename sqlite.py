import sqlite3
import sys
from sqlite3 import Connection, Error

from conui import Contact


def connect() -> Connection:
    try:
        conn = sqlite3.connect("data.sqlite")
        return conn
    except Error as err:
        print("Error to connect database", err)


def create_table(data: Connection):  # data est la connexion à la db
    sql = """CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                f_name TEXT,
                l_name TEXT NOT NULL ,
                tel TEXT
             );"""
    cursor = data.cursor()  # on crée un cursor
    cursor.execute(sql)  # exécution de la query
    data.commit()  # valider les changements sur le disque


def exists(data, contact):
    return None


def findall(data:Connection) -> list[[Contact]]:
    sql = """SELECT f_name,l_name, tel FROM contacts"""
    data.row_factory = lambda cursor, row: Contact(row[0], row[1], row[2])
    cursor = data.cursor()
    cursor.execute(sql)
    #rows = cursor.fetchall()
    #contacts = []
    #for row in rows:
    #    contacts.append(Contact(row[0],row[1],row[2]))
    #return contacts
    return cursor.fetchall()

def search(data, part_name):
    return None


def delete(data, contact):
    return None


def update(data, old_contact, new_contact):
    return None


def load():
    try:
        conn = connect()
        create_table(conn)
        return conn
    except Error as err:
        print("Unable to create database")
        sys.exit(-1)


def save(data: Connection):  # data est la db
    data.commit()


def create(data: Connection, contact: Contact) -> int:
    sql = """INSERT INTO contacts (f_name, l_name, tel) VALUES (?,?,?)"""
    cursor = data.cursor()
    cursor.execute(sql, contact)  # on passe IMPÉRATIVEMENT un tuple !!
    data.commit()
    return cursor.lastrowid


def read(data:Connection, id:int) -> Contact:
    sql = """SELECT f_name,l_name,tel FROM contacts WHERE id = ?"""
    data.row_factory = lambda cursor, row: Contact(row[0],row[1],row[2])
    cursor = data.cursor()
    cursor.execute(sql,(id,)) # on passe un tuple
    #row = cursor.fetchone()
    #return Contact(row[0],row[1],row[2])
    return cursor.fetchone()
