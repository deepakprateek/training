from db_connection import get_db
from queries import *


def insertdata(data):
    """
    This Function Inserts Data Into Table
    :param data:
    :return: Result(True or False)
    """
    db = get_db()
    cursor = db.cursor()
    cursor.executemany(query_insert_data,
                       data)
    db.commit()
    return True


def updaterecord(id, First_Name, Last_Name, Company_Name, Branch):
    """
    This Function Modifies Records By Matching ID
    :param id:
    :param First_Name:
    :param Last_Name:
    :param Company_Name:
    :param Branch:
    :return:Result(True or False)
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query_update_recs, [First_Name, Last_Name, Company_Name, Branch, id])
    db.commit()
    return True


def deleterecord(id):
    """
    This Function Deletes The Record Of Matched ID
    :param id:
    :return:Result(True or False)
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query_delete_record, [id])
    db.commit()
    return True


def getallrecords():
    """
    This Function Return All Records From Table
    :return:
    """
    db = get_db()
    cursor = db.cursor()
    allrecords = []
    for row in cursor.execute(query_get_all_recs):
        record = {}
        record.setdefault("ID", row[0])
        record.setdefault("First_Name", row[1])
        record.setdefault("Last_Name", row[2])
        record.setdefault("Company_Name", row[3])
        record.setdefault("Branch", row[4])
        allrecords.append(record)
    return allrecords
