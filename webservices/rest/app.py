from flask import Flask, jsonify, request
import db_controller
from db_connection import create_tables

app = Flask(__name__)

create_tables()


@app.route('/getallrecords', methods=["GET"])
def get_records():
    """
    This Function Return All Records From Table
    :return:
    """
    records = db_controller.getallrecords()
    return jsonify({"records": records})


@app.route('/deleterecord/<ID>', methods=["DELETE"])
def delete_record(ID):
    """
    This Function Deletes The Record Of Matched ID
    :param ID:
    :return:Result(True or False)
    """
    result = db_controller.deleterecord(ID)
    return jsonify({"result": result})


@app.route('/updaterecord', methods=["PUT"])
def update_record():
    """
    This Function Modifies Records By Matching ID
    :return: Result(True or False)
    """
    details = request.get_json()
    ID = details["ID"]
    First_Name = details["First_Name"]
    Last_Name = details["Last_Name"]
    Company_Name = details["Company_Name"]
    Branch = details["Branch"]
    result = db_controller.updaterecord(ID, First_Name, Last_Name, Company_Name, Branch)
    return jsonify({"result": result})


@app.route('/insertdata', methods=["POST"])
def inset_records():
    """
    This Function Inserts Data Into Table
    :return:Result(True or False)
    """
    details = request.get_json()
    data = []
    for i in details["data"]:
        data.append(tuple(i))
    result = db_controller.insertdata(data)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()
