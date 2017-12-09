import datetime
import os
import traceback
import logging
import psycopg2 as dbapi2
from flask import render_template
from flask import Flask
from flask import redirect
from flask.helpers import url_for

app = Flask(__name__)

class Student:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS student_table (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(30) NOT NULL,
                            surname VARCHAR(30) NOT NULL,
                            email VARCHAR(30) UNIQUE
                            )
                            """
                cursor.execute(query)

                connection.commit()

    def insert_student(self, name, surname, email):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO student_table VALUES
                        (DEFAULT,(%s),(%s),(%s)) """
            param = (name, surname, email)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_student(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM student_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_student(self, id, new_name, new_surname, new_email):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE student_table SET name = (%s), surname = (%s), email = (%s)
                        WHERE id = (%s) """
            param = (new_name, new_surname, new_email, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_student_id(self, name, surname):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM student_table WHERE
                        (name = (%s) AND surname = (%s)) """
            param = (name, surname)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_student(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM student_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)

            student = cursor.fetchone()
            
            connection.commit()

            return student
        
