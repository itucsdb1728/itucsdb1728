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

class Classroom:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS classroom_table (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(7) NOT NULL,
                            year INTEGER NOT NULL CHECK (year >= 2012 AND year<=2053)
                            )
                            """
                cursor.execute(query)
                connection.commit()
                
    def insert_classroom(self, classroom_name, year):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO classroom_table VALUES
                        (DEFAULT,(%s),(%s)) """
            param = (classroom_name, year)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_classroom(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM classroom_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_classroom(self, id, new_classroom_name, new_year):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE classroom_table SET name = (%s), year = (%s)
                        WHERE id = (%s) """
            param = (new_classroom_name, new_year, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_classroom_id(self, classroom_name, year):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM classroom_table WHERE
                        (name = (%s) AND year = (%s)) """
            param = (classroom_name, year)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_classroom(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM classroom_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)

            classroom = cursor.fetchone()
            
            connection.commit()

            return classroom
        
        

