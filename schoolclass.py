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

class SchoolClass:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS school_class_table (
                            id SERIAL PRIMARY KEY,
                            class_id INTEGER NOT NULL REFERENCES classroom_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            school_id INTEGER NOT NULL REFERENCES schools_table(id) ON DELETE CASCADE ON UPDATE CASCADE
                            )
                            """
                cursor.execute(query)

                connection.commit()

    def insert_school_class(self, class_id, school_id):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO school_class_table VALUES
                        (DEFAULT,(%s),(%s)) """
            param = (class_id, school_id)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_school_class(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM school_class_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_school_class(self, id, new_class_id, new_school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE school_class_table SET class_id = (%s), school_id = (%s)
                        WHERE id = (%s) """
            param = (new_class_id, new_school_id ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_school_class_id(self, class_id, school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM school_class_table WHERE
                        (class_id = (%s) AND school_id = (%s)) """
            param = (class_id, school_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id
        

