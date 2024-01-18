import sqlite3

DATABASE_NAME = "crud_db.db"


def get_db():
    """
    This Function Establishes The Connection With Database
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    """
    This Function Creates The Table If The Table Not Exists
    :return:
    """
    tables = [
        '''CREATE TABLE IF NOT EXISTS peoples(
            ID integer PRIMARY KEY AUTOINCREMENT,
            First_Name text,
            Last_Name text,
            Company_Name text,
            Branch text);'''
             ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
