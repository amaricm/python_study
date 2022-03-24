
import mysql.connector
from datetime import date, timedelta, datetime
from task import Task

class Todo(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="todo"
        )

    def new_task(self, task, start_date=None):
        if not start_date:
            start_date = datetime.now()

        cursor = self.mydb.cursor()

        cursor.execute("""
            Insert into todo_list
                (start_date, name_task, description_task)
                VALUES (%s, %s, %s)
        """, [start_date, task.name, task.description])
        
        self.mydb.commit() 

        return cursor.lastrowid

    def complete_task(self, id_task, complete_date=None):
        if not complete_date:
            complete_date = datetime.now()

        cursor = self.mydb.cursor()

        cursor.execute("""
                UPDATE todo_list SET 
                    complete_date = %s,
                    mark_complete =%s
                where todo_list.id = %s
            """, [complete_date, True, id_task])
        self.mydb.commit()

    def get_tasks(self): 
        cursor = self.mydb.cursor()

        cursor.execute(" select * from todo_list where mark_complete is null")
        results = cursor.fetchall()
        tasks = []
        for record in results:
            tasks.append(Task(record[0],record[2], record[5]))
        return tasks   
    




     

 