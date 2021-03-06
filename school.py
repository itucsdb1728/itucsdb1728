
import datetime
import os
import traceback
import logging
import psycopg2 as dbapi2
#import sys
from flask import render_template
from flask import Flask
from flask import redirect
from flask.helpers import url_for

app = Flask(__name__)

class School:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS school_table(
                id SERIAL primary key,
                school_name varchar(100) not null)"""
            
            cursor.execute(query)

    def insert_school(self, school_name):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO schools_table VALUES
                        (DEFAULT,(%s)) """
            param = (school_name,)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_school(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM schools_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_school(self, id, new_school_name):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE schools_table SET school_name = (%s)
                        WHERE id = (%s) """
            param = (new_school_name, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_school_id(self, school_name):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM schools_table WHERE
                        (school_name = (%s)) """
            param = (school_name,)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_school(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM school_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)

            school = cursor.fetchone()
            
            connection.commit()

            return school   
