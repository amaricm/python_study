from flask import Flask, jsonify, request, json
from quickbooks import Quickbook
from company import Company
import mysql.connector

app = Flask(__name__)
app.debug = True
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="Company"
        )

@app.route("/companies", methods=['GET'])
def get_all_companies():    
    quickbook_a = Quickbook(mydb)
    companies = quickbook_a.get_all_companies()

    companies_json = []
    
    for company in companies:
        companies_json.append(
            {
                "id": company.get_id(),
                "name": company.name
            }
        )

    return jsonify(companies_json)

@app.route("/companies/<id>", methods=['GET'])
def get_company_by_id(id):

    quickbook_a = Quickbook(mydb)
    company = quickbook_a.get_company_by_id(id)
    
    return jsonify(
        {
            "id": company.get_id(),
            "name": company.name
        }
    )

     
@app.route('/companies', methods=['POST'])
def add_company():
    data = json.loads(request.data)
    quickbook_a = Quickbook(mydb)
    quickbook_a.new_company(data["name"], data["cash"])

    return data

@app.route("/companies/<id>", methods=['PUT'])
def update_company(id):
    data = json.loads(request.data)
    name = data["name"]
    cash = data["cash"]
    quickbook_a = Quickbook(mydb)
    company1 = Company(int(id), name, cash,None)
    quickbook_a.update_company(company1)

    return data
    
@app.route("/companies/<id>", methods=['DELETE'])
def delete_company(id):
    quickbook_a = Quickbook(mydb)
    company = quickbook_a.get_company_by_id(id)
    quickbook_a.delete_company(id)
    return jsonify(
        {
            "id": company.get_id(),
            "name": company.name
        }
    )
    
#people

@app.route("/people", methods=['GET'])
def get_all_people():    
    quickbook_a = Quickbook(mydb)
    people = quickbook_a.get_all_people()

    people_json = []
    
    for person in people:
        people_json.append(
            {
                "id": person.get_id(),
                "name": person.name,
                "last_name": person.last_name,
                "email": person.email
            }
        )

    return jsonify(people_json)
     
@app.route("/people/<id>", methods=['GET'])
def get_people_by_id(id):

    quickbook_a = Quickbook(mydb)
    person = quickbook_a.get_people_by_id(id)
    
    return jsonify(
         {
                "id": person.get_id(),
                "name": person.name,
                "last_name": person.last_name,
                "email": person.email
            }
        )

@app.route('/people', methods=['POST'])
def add_person():
    data = json.loads(request.data)
    quickbook_a = Quickbook(mydb)
    quickbook_a.new_person(data["name"], data["last_name"], data["email"])

    return data