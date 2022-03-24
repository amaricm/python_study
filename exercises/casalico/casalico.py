import unittest
import mysql.connector

from model.user import User
from model.property import Property
from model.sales_record import Sales_Record
from model.photo_property import Photos_Property

from datetime import datetime, timedelta

class UserDB:

    def __init__(self, db_connector):
        self.mydb = db_connector

    def new_user(self,name,last_name,email, phone, user_type):
   
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into user
                (name, last_name,email,phone, user_type)
                VALUES (%s, %s, %s, %s, %s)
        """, [name, last_name, email, phone, user_type])
        self.mydb.commit()

        return User(
            cursor.lastrowid, name, last_name, email, phone, user_type)

    def get_users_by_user_type(self, user_type):
        cursor = self.mydb.cursor()
        if user_type: 
            cursor.execute("select * from user where user_type=%s", [user_type])
        else:
            cursor.execute("select * from user")

        records = cursor.fetchall()

        users = []
        if len(records) > 0:              
            for record_user in records:
                user = User(
                    record_user[0],
                    record_user[1], 
                    record_user[2], 
                    record_user[3],
                    record_user[4],
                    record_user[5]
                )
                users.append(user)
        return users

    def get_user_by_login(self, login):
        cursor = self.mydb.cursor()
        
        cursor.execute("select * from user where login=%s", [login])
        record_user = cursor.fetchone()

        if not record_user:
            return None

        return User(
            record_user[0],
            record_user[1], 
            record_user[2], 
            record_user[3],
            record_user[4],
            record_user[5],
            record_user[6],
            record_user[7]
        )



class OwnerDB:

    def __init__(self, db_connector):
        self.mydb = db_connector



class PropertyDB:  
    def __init__(self, db_connector):
        self.mydb = db_connector

    def get_all_properties(self):
        cursor = self.mydb.cursor()
        cursor.execute("select * from property")
        records = cursor.fetchall()

        results = []
        for record in records:
                results.append(Property(
                    record[1],  # owner_id
                    record[2],  # number_of_rooms
                    record[3],  # number_of_bathrooms
                    record[4],  # sqft
                    record[5],  # lote
                    record[6],  # price
                    record[7],  # street
                    record[8],  # city
                    record[9],  # zip_code
                    record[11], # realtor id
                    record[12], # year_of_construction
                    record[11], # status
                    record[10], # create_date,
                    record[0]   # id
            ))

        return results

    def get_property_by_id(self, property_id):
        cursor = self.mydb.cursor()
        cursor.execute("select * from property where id=%s", [property_id])
        record = cursor.fetchone()

        if not record:
            return None

        return Property(
            record[1],  # owner_id
            record[2],  # number_of_rooms
            record[3],  # number_of_bathrooms
            record[4],  # sqft
            record[5],  # lote
            record[6],  # price
            record[7],  # street
            record[8],  # city
            record[9],  # zip_code
            record[11], # realtor id
            record[12], # year_of_construction
            record[11], # status
            record[10], # create_date,
            record[0]   # id
        )

    def insert_photo(self,property_id,image_path):
   
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into photos_property
                (property_id, image_path)
                VALUES (%s, %s)
        """, [property_id, image_path ])
        self.mydb.commit()

        return Photos_Property(
            cursor.lastrowid, property_id, image_path)

  
    def get_photo_by_id(self, property_id):
        cursor = self.mydb.cursor()
        cursor.execute("select * from photos_property where id=%s", [property_id])
        record = cursor.fetchone()

        return Photos_Property(
            record[2],
            record[0],
            record[1]
        )

    def order_properties_by_price(self, properties, order):
        results = []
        for property in properties:
            added = False
            for i in range(len(results)):
                if order == "asc" and property.price < results[i].price or order == "desc" and property.price > results[i].price:
                    results.insert(i, property)
                    added = True
                    break

            if not added:
                results.append(property) 
        return results

    
    def create_property(self, property):
        create_date = datetime.now()
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into property
                (owner_id,number_of_rooms,number_of_bathrooms,sqft, lote, price, street, city, zip_code, create_date,realtor_id, year_of_construction, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [  
                property.owner_id, property.number_of_rooms, property.number_of_bathrooms, property.sqft, property.lote, 
                property.price, property.street, property.city, 
                property.zip_code, create_date, property.realtor_id, property.year_of_construction, property.status
            ])
                
        self.mydb.commit()

        property.set_id(cursor.lastrowid)
        property.create_date = create_date

        return property

    def update_property(self, property):
        cursor = self.mydb.cursor()
        cursor.execute(""" update property set
                                owner_id = %s,
                                number_of_rooms= %s,
                                number_of_bathrooms = %s, 
                                sqft = %s, 
                                lote = %s, 
                                price = %s, 
                                street = %s, 
                                city = %s, 
                                zip_code = %s, 
                                create_date = %s,
                                realtor_id = %s, 
                                year_of_construction = %s, 
                                status = %s 
                            where id = %s
                        """, [
                            property.owner_id,
                            property.number_of_rooms,
                            property.number_of_bathrooms,
                            property.sqft,
                            property.lote,
                            property.price,
                            property.street,
                            property.city,
                            property.zip_code,
                            property.create_date,
                            property.realtor_id,
                            property.year_of_construction,
                            property.status,
                            property.get_id()
                        ])
        self.mydb.commit()
        return property

    # def update_realtor(self, property_id, realtor_id):
    #     cursor = self.mydb.cursor()
    #     cursor.execute("update Property set realtor_id = %s where id=%s", 
    #         [realtor_id, property_id])
    #     self.mydb.commit()

    def update_user(self, id):
        cursor = self.mydb.cursor()
        cursor.execute("""update user set 
                            name = %s,
                            last_name = %s,
                            email = %s,
                            phone = %s,

                            where id=%s
                            """, [
                        user.name,
                        user.last_name,
                        user.email,
                        user.phone,
                        ])
        self.mydb.commit()
        return user


class RealtorOperations:
    
    def __init__(self, db_connector):
        self.mydb = db_connector
        

    
    def add_photo(self,property_id, image_path):
        
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into photo_property
                (property_id, image)
                VALUES (%s, %s)
        """, [property_id, image])

        self.mydb.commit()

        return photo_property(cursor.lastrowid,property_id,image_path)
 
    def delete_property(self,property_id):
        cursor = self.mydb.cursor()
        cursor.execute("select from photos_property where id=%s", [property_id])
        self.mydb.commit()



    def sales_record(self,property_id,realtor_id,sale_price,month_of_sale):
        create_date = datetime.now()
    
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into sales_record
                (property_id,realtor_id,sale_price,month_of_sale)
                VALUES (%s, %s, %s, %s)
        """, [property_id,realtor_id,sale_price,month_of_sale])
        self.mydb.commit()

        sales_record = Sales_Record(cursor.lastrowi,property_id,realtor_id,sale_price,month_of_sale)

        return sales_record





# class Clasalico:
#     def __init__(self, db_connector):
#         self.mydb = db_connector

#     def new_property(self,id,number_of_rooms,number_of_bathroom,sqft, lote, price, street, city, zip_code):
#         create_date = datetime.now()
    
#         cursor = self.mydb.cursor()
#         cursor.execute("""
#             Insert into property
#                 (name, number_of_rooms,number_of_bathroom,sqft, lote, price, street, city, zip_code, create_date)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)
#         """, [property.name, property.number_of_rooms, property.number_of_bathroom, property.sqft, property.lote, property.price, property.street, property.city, property.zip_code, property.create_date])
#         self.mydb.commit()

#         property = Property(
#             cursor.lastrowid, name, number_of_rooms,number_of_bathroom,sqft,
#             lote, price, street, city, zip_code, create_date)

#         return property








    
     