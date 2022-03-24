from flask import Flask, jsonify, request, json, g
from flask import send_file
from casalico import UserDB, PropertyDB
from model.property import Property

import mysql.connector

app = Flask(__name__)
app.debug = True

class AuthenticationException(Exception):
    pass

class AuthorizationException(Exception):
    pass

class ValidationException(Exception):
    pass


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'my_db'):
        g.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="casalico"
        )
    return g.my_db        

def authorization(user, user_type):
    if user.user_type != user_type:
        raise AuthorizationException()

def authentication(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        raise AuthenticationException()
    
    credentials = auth_header.split(":")

    login = credentials[0]
    password = credentials[1]

    user_db = UserDB(get_db())
    user = user_db.get_user_by_login(login)

    if not user or user.password != password:
        raise AuthenticationException()

    return user

def validate_user(request):
    pass

#################USERS#########################
#
#
#
#
#
#
#################USERS#########################

@app.route('/users', methods=['POST'])
def create_user():
    try:
        validate_user(request)
        data = json.loads(request.data)
        user = UserDB(get_db())
        user = user.new_user(data["name"], data["last_name"], data["email"], data["phone"], data["user_type"])

        return jsonify(
            {
                    "id": user.get_id(),
                    "name": user.name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "phone": user.phone,
                    "user_type": user.user_type
                }
            )
    except AvalidationException:
        return { "error": "wrong requiere format" }, 400

@app.route('/users', methods=['GET'])
def get_users_by_type():
    user_type = request.args.get('user_type')
    user = UserDB(get_db())
    users = user.get_users_by_user_type(user_type)

    users_json = []
    
    for user in users:
        users_json.append(
            {
                "id": user.get_id(),
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email,
                "phone": user.phone,
                "user_type": user.user_type
            }
        )

    return jsonify(users_json)


#################PROPERTIES#########################
#
#
#
#
#
#
#################PROPERTIES#########################
@app.route('/properties', methods=['GET'])
def get_all_properties():

    order = request.args.get('order', "asc")
    min_price = int(request.args.get('min_price',0))
    max_price = int(request.args.get('max_price',10**20))
    
    property_db = PropertyDB(get_db())
    properties = property_db.get_all_properties()
    sort_properties = property_db.order_properties_by_price(properties, order)

    json_result = []

    for property in sort_properties:
        if property.price > min_price and property.price < max_price:
            json_result.append({
                "id": property.get_id(),
                "owner_id": property.realtor_id,   
                "realtor_id": property.realtor_id,
                "number_of_rooms": property.number_of_rooms,
                "number_of_bathrooms": property.number_of_bathrooms, 
                "sqft": property.sqft, 
                "lote": property.lote, 
                "price": property.price,
                "street": property.street, 
                "city": property.city, 
                "zip_code": property.zip_code
            })

    return jsonify(
        json_result
    )
    

@app.route('/properties/<id>', methods=['GET'])
def get_property_by_id(id):
    property_db = PropertyDB(get_db())
    property = property_db.get_property_by_id(id)

    return jsonify(
         {
            "id": property.get_id(),
            "owner_id": property.realtor_id,   
            "realtor_id": property.realtor_id,
            "number_of_rooms": property.number_of_rooms,
            "number_of_bathrooms": property.number_of_bathrooms, 
            "sqft": property.sqft, 
            "lote": property.lote, 
            "price": property.price,
            "street": property.street, 
            "city": property.city, 
            "zip_code": property.zip_code
         }
    )

@app.route('/properties', methods=['POST'])
def create_property():
    try:
        user = authentication(request)
        authorization(user, "realtor")
        property = json.loads(request.data, object_hook=lambda d: Property(**d))

        data = json.loads(request.data)
        property_db = PropertyDB(get_db())
        property = property_db.create_property(property)       

        return jsonify(
            {
                "id": property.get_id(),
                "owner_id": property.realtor_id,   
                "realtor_id": property.realtor_id,
                "number_of_rooms": property.number_of_rooms,
                "number_of_bathrooms": property.number_of_bathrooms, 
                "sqft": property.sqft, 
                "lote": property.lote, 
                "price": property.price,
                "street": property.street, 
                "city": property.city, 
                "zip_code": property.zip_code
            }
        )
    except AuthenticationException:
        return { "error": "you must be authenticated" }, 401
    except AuthorizationException:
        return { "error": "You dont have permissions to create property" }, 403

@app.route("/properties/<id>", methods=['PUT'])
def update_property(id):
    request_property = json.loads(request.data, object_hook=lambda d: Property(**d))
    request_property.set_id(id)

    property_db = PropertyDB(get_db())
    existent_db_property = property_db.get_property_by_id(id)

    if not existent_db_property:
        return { "error": "Property not found" }, 404

    property = property_db.update_property(request_property)

    return jsonify(
            {
                "id": property.get_id(),
                "owner_id": property.realtor_id,   
                "realtor_id": property.realtor_id,
                "number_of_rooms": property.number_of_rooms,
                "number_of_bathrooms": property.number_of_bathrooms, 
                "sqft": property.sqft, 
                "lote": property.lote, 
                "price": property.price,
                "street": property.street, 
                "city": property.city, 
                "zip_code": property.zip_code
            }
        )

@app.route("/properties/<id>", methods=['DELETE'])
def delete_property(id):
    property_db = PropertyDB(get_db())
    property = property_db.get_property_by_id(id)
    property_db.delete_property(id)

    return jsonify(
         {
            "id": property.get_id(),
            "owner_id": property.realtor_id,   
            "realtor_id": property.realtor_id,
            "number_of_rooms": property.number_of_rooms,
            "number_of_bathrooms": property.number_of_bathrooms, 
            "sqft": property.sqft, 
            "lote": property.lote, 
            "price": property.price,
            "street": property.street, 
            "city": property.city, 
            "zip_code": property.zip_code
         }
    )

#################USERS#########################
#
#
#
#
#
#
#################USERS#########################
@app.route("/user/<id>", methods=['PUT'])
def update_user(id):
    data = json.loads(request.data)
    
    property_db = PropertyDB(get_db())
    user = property_db.update_user(id)

    if data.get("name", None):
        property.name = data["name"]
    if data.get("last_name", None):
        property.last_name = data["last_name"]
    if data.get("email", None):
        property.email = data["email"]
    if data.get("phone", None):
        property.phone = data["phone"]
    
    property_db.update_user(user)

    return data

#################PHOTOS#########################
#
#
#
#
#
#
#################PHOTOS#########################
@app.route("/photos", methods=['POST'])
def create_photo():
    data = json.loads(request.data)
    
    property_db = PropertyDB(get_db())
    photo_property = property_db.insert_photo(data["property_id"],
        data["image_path"])

    return jsonify(
         {
            "id": photo_property.get_id(),
            "property_id": photo_property.property_id,
            "image_path": photo_property.image_path   
         }
    )

@app.route('/photos/<id>', methods=['GET'])
def get_photo_by_id(id):
    property_db = PropertyDB(get_db())
    photo_property = property_db.get_photo_by_id(id)

    return send_file(photo_property.image_path, mimetype='image/jpg')
