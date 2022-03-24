import unittest
import mysql.connector
from person import Person
from company import Company
from account_payable import Account_Payable
from account_receivable import Account_Receivable
from datetime import datetime, timedelta

class Quickbook:
    def __init__(self, db_connector):
        self.mydb = db_connector

    def new_company(self, company_name, cash):
        registry_date = datetime.now()
    
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into Company
                (name, cash, registry_date)
                VALUES (%s, %s, %s)
        """, [company_name, cash, registry_date])
        self.mydb.commit()

        company = Company(cursor.lastrowid, company_name, cash, registry_date)

        return company

    def add_employee_to_company(self, company, person, salary):
        
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into Person
                (name, last_name, email)
                VALUES (%s, %s, %s)
        """, [person.name, person.last_name, person.email])

        self.mydb.commit()

        person.id = cursor.lastrowid
        
        cursor.execute("""
            Insert into Person_Company
                (company_id, person_id, salary, active)
                VALUES (%s, %s, %s, %s)
        """, [company.get_id(), person.id, salary, True])

        self.mydb.commit()

    def add_account_receivable(self, account_receivable):
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into Account_Receivable
                (description, amount, due_date, to_company_id, from_company_id)
                VALUES (%s, %s, %s, %s, %s)
        """, [
            account_receivable.description, 
            account_receivable.amount, 
            account_receivable.due_date,  
            account_receivable.to_company_id, 
            account_receivable.from_company_id])

        self.mydb.commit()

        account_receivable.set_id( cursor.lastrowid)   
        return account_receivable

    def add_account_payable(self, account_payable):
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into Account_Payable
                (description, amount, due_date, priority, to_company_id, from_company_id)
                VALUES (%s, %s, %s, %s, %s, %s)
        """, [
            account_payable.description, 
            account_payable.amount, 
            account_payable.due_date, 
            account_payable.priority, 
            account_payable.to_company_id, 
            account_payable.from_company_id])

        self.mydb.commit()

        account_payable.set_id(cursor.lastrowid)
        return account_payable

    def get_all_companies(self):
        cursor = self.mydb.cursor()
        cursor.execute("select * from Company")
        records = cursor.fetchall()

        companies = []

        for record_company in records:
            companies.append(Company(record_company[0],record_company[1], record_company[2], record_company[3]))
        
        return companies


    def get_all_people(self):
        cursor = self.mydb.cursor()
        cursor.execute("select * from Person")
        records = cursor.fetchall()

        people = []

        for record_person in records:
            people.append(Person(record_person[0],record_person[1], record_person[2], record_person[3]))
        
        return people
        

    def get_company_by_id(self, id):
        cursor = self.mydb.cursor()
        cursor.execute("select * from Company where id=%s", [id])
        record = cursor.fetchone()

        if not record:
            return None
        else:
            return Company(record[0],record[1], record[2], record[3])

    def get_company(self, name):

        cursor = self.mydb.cursor()
        cursor.execute("select *  from Company where name=%s", [name])
        record = cursor.fetchone()
        
        if not record:
            return None
        else:
            return Company(record[0],record[1], record[2], record[3])

    def get_employee(self, email):
        cursor = self.mydb.cursor()
        cursor.execute("select *  from Person where email=%s", [email])
        record = cursor.fetchone()

        if not record:
            return None
        return Person(record[0],record[1], record[2], record[3])

    def get_people_by_id(self, id):
        cursor = self.mydb.cursor()
        cursor.execute("select *  from Person where id=%s", [id])
        record = cursor.fetchone()

        if not record:
            return None
        return Person(record[0],record[1], record[2], record[3])       

    def new_person(self, name, last_name, email):  
        cursor = self.mydb.cursor()
        cursor.execute("""
            Insert into Person
                (name, last_name, email)
                VALUES (%s, %s, %s)
        """, [name, last_name, email])
        self.mydb.commit()

        person = Person(cursor.lastrowid, name, last_name, email)

        return person





    def update_company(self, company):
        cursor = self.mydb.cursor()
        cursor.execute("update Company set name = %s, cash = %s  where id=%s", 
            [company.name, company.cash,company.get_id()])
        self.mydb.commit()

    def delete_company(self, id):
        cursor = self.mydb.cursor()
        cursor.execute("delete from Person_Company where company_id=%s",[id] )   
        cursor.execute("delete from Account_Receivable where to_company_id=%s",[id])   
        cursor.execute("delete from Account_Payable where from_company_id=%s", [id])  
        cursor.execute("delete from Company where id=%s", [id])          
        self.mydb.commit()
        
    def onboard_company(self, name, cash, employee_list, ap_list, ar_list):
        # onboarding company
        company = self.new_company(name, cash) 

        # onboarding employees
        self.onboard_employees(company, employee_list)

        # onboarding account payable
        self.onboard_account_payable(company, ap_list)

        # onboarding account receivable
        self.onboard_account_receivable(company, ar_list)

    def onboard_employees(self, company, employee_list):
        """employee_list is a list of lists [ name, last_name, email, salary ]"""
        
        for e in employee_list:
            person = Person(None, e[0], e[1], e[2])
            self.add_employee_to_company(company, person, e[3])

    def onboard_account_payable(self, company, ap_list):
        """ar_list is a list of lists [ description, amount, due_date, priority, to_company_name ]"""
        for ap in ap_list:
            company_to = self.get_company(ap[4])
            if not company_to:
                company_to = self.new_company(ap[4], 0) 
            account_payable = Account_Payable(None,ap[0], ap[1], ap[2], ap[3], company_to.get_id(),  company.get_id() )
            self.add_account_payable( account_payable)
   
    def onboard_account_receivable(self, company, ar_list):
        """ap_list is a list of lists [ description, amount, due_date, from_company_name ]"""
        for ar in ar_list:
            company_from = self.get_company(ar[3])
            if not company_from:
                company_from = self.new_company(ar[3], 0) 
            account_receivable = Account_Receivable(None,ar[0], ar[1], ar[2], company.get_id(), company_from.get_id() )
            self.add_account_receivable( account_receivable)

    def employees_per_company(self, company_name):

        cursor = self.mydb.cursor()

        cursor.execute("""
            select count(Person.id) as num_employee
                from Person
                join Person_Company on Person.id = Person_Company.person_id
                join Company on Company.id = Person_Company.company_id
            where Company.name = %s """, [company_name])
        record = cursor.fetchone()
        return record[0]
         
    def generate_payroll(company_name):
        cursor = self.mydb.cursor()

        company = self.get_company(company_name)

        cursor.execute("""
            select sum(Person_Company.salary) 
                from Person_Company
                join Company on Company.id = Person_Company.company_id
                where Company.id = %s and Person_Company.active = 1
                """, [company.get_id()])
        record = cursor.fetchone()
        total_salary = record[0]

        cursor.execute("""
            insert into Account_Payable
            (description, amount, due_date, priority, to_company_id, from_company_id ) 
                VALUES (%s, %s, %s, %s, %s, %s)""", [
            "salary", 
            total_salary, 
            datetime.strptime("2022-02-28", "%Y-%m-%d"), 
            5, 
            company.get_id(), 
            company.get_id() ])

        self.mydb.commit()

    # def to_pay_payroll(self):
    #     registry_date = datetime.now()

    #     cursor = self.mydb.cursor()

    #     cursor.execute("""
    #         select  sum(Account_Payable.amount)
    #         from Account_Payable
    #         where Account_Payable.due_date = %s and Account_Payable.priority = 5 
    #             """, [registry_date])
    #             record = cursor.fetchone()
    #             total_salary = record[0]
        




        
class TestOnboarding(unittest.TestCase):  
    @classmethod
    def setUpClass(cls):
        cls.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="Company"
        )

        # We always delete the database first
        cls.delete_database()
  
        employee_list =[
            ["Javier", "de Paula", "jdp@gmail.con", 400], 
            ["Rosa", "Suarez", "sdf@gmail.con", 300],
            ["Pablo", "Garcia", "pg@gmail.con", 200],
            ["Amelia", "Lopez", "alp@gmail.con", 100],
            ["Juan", "Rosabal", "rsb@gmail.con", 150],
        ]
             
        ap_list = [
            ["d1", 20, datetime.strptime("2022-02-28", "%Y-%m-%d"), 1, "Cemento"],
            ["d2", 40, datetime.strptime("2022-02-27", "%Y-%m-%d"), 1, "Metal"],
            ["d3", 50, datetime.strptime("2022-02-28", "%Y-%m-%d"), 1, "Roma"],
            ["d4", 60, datetime.strptime("2022-02-25", "%Y-%m-%d"), 1, "Opa"],
            ["d5", 10, datetime.strptime("2022-02-20", "%Y-%m-%d"), 1, "Seta"],
        ]

        ar_list = [ 
            ["c1", 15, datetime.strptime("2022-02-26", "%Y-%m-%d"), "Agua"],
            ["c1", 13, datetime.strptime("2022-02-26", "%Y-%m-%d"), "Arena"],
            ["c1", 16, datetime.strptime("2022-02-26", "%Y-%m-%d"), "Pez"],
        ]

        cls.quickbook_1 = Quickbook(cls.mydb)
        cls.quickbook_1.onboard_company("Apple", 100000, employee_list, ap_list, ar_list)  

    def test_get_employees(self):
        quickbook = TestOnboarding.quickbook_1

        assert quickbook.employees_per_company("Apple") == 5

    def test_payroll(self):
        quickbook = TestOnboarding.quickbook_1

        quickbook.generate_payroll("Apple") 

        company = self.get_company(company_name)

        cursor = self.mydb.cursor()

        cursor.execute("""
            select Account_Payable.* 
            from Account_Payable
            join Company
            where Account_Payable.description = "salary"
            and where Company.id = %s
       
                """)
        record = cursor.fetchall()
     
        
       
        

    @classmethod
    def tearDownClass(cls): 
        #cls.delete_database()
        pass

    @classmethod
    def delete_database(cls):
        cursor = cls.mydb.cursor()
        cursor.execute("delete  from Account_Payable")
        cursor.execute("delete  from Account_Receivable")
        cursor.execute("delete  from Person_Company")
        cursor.execute("delete  from Person")
        cursor.execute("delete  from Company")
        cls.mydb.commit()


if __name__ == '__main__':
    unittest.main()




    
