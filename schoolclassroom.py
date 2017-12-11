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

class SchoolClassroom:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS school_classroom_table (
                            id SERIAL PRIMARY KEY,
                            classroom_id INTEGER NOT NULL REFERENCES classroom_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            school_id INTEGER NOT NULL REFERENCES schools_table(id) ON DELETE CASCADE ON UPDATE CASCADE
                            )
                            """
                cursor.execute(query)

                connection.commit()

    def insert_school_classroom(self, classroom_id, school_id):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO school_classroom_table VALUES
                        (DEFAULT,(%s),(%s)) """
            param = (classroom_id, school_id)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_school_classroom(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM school_classroom_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_school_classroom(self, id, new_classroom_id, new_school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE school_classroom_table SET classroom_id = (%s), school_id = (%s)
                        WHERE id = (%s) """
            param = (new_classroom_id, new_school_id ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_school_classroom_id(self, classroom_id, school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM school_classroom_table WHERE
                        (classroom_id = (%s) AND school_id = (%s)) """
            param = (classroom_id, school_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id
    
    def get_clasrooms_school(self, classroom_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT school_id FROM school_classroom_table WHERE
                        (classroom_id = (%s)) """
            param = (classroom_id,)
            
            cursor.execute(query,param)

            school_id = cursor.fetchone()
            
            connection.commit()

            return school_id
        
    def get_schools_all_classrooms(self, school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT classroom_id FROM school_classroom_table WHERE
                        (school_id = (%s)) """
            param = (school_id,)
            
            cursor.execute(query,param)

            classrooms = cursor.fetchall()
            
            connection.commit()

            return classrooms
        

