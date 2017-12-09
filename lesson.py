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

class Lesson:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS lesson_table (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(50) NOT NULL
                            )
                            """
                cursor.execute(query)

                connection.commit()
    
    def insert_lesson(self, lesson_name):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO lesson_table VALUES
                        (DEFAULT,(%s)) """
            param = (lesson_name,)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_lesson(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM lesson_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_lesson(self, id, new_lesson_name):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE lesson_table SET name = (%s)
                        WHERE id = (%s) """
            param = (new_lesson_name, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_lesson_id(self, lesson_name):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM lesson_table WHERE
                        (name = (%s)) """
            param = (lesson_name,)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_lesson(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM lesson_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)

            lesson = cursor.fetchone()
            
            connection.commit()

            return lesson
        
        

