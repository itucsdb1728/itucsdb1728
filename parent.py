
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

class Parent:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
       
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS parent_table(
                        id SERIAL primary key,
                        name VARCHAR(60) not null,
                        surname VARCHAR(60) not null,
                        phone_number varchar(15),
                        email VARCHAR(60))"""
           
            cursor.execute(query)

            connection.commit()
    
    def insert_parent(self, parent_name, parent_surname, parent_phone_number = None, parent_email = None):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO parent_table VALUES
                        (DEFAULT,(%s),(%s),(%s),(%s)) """
            param = (parent_name, parent_surname, parent_phone_number, parent_email)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_parent(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM parent_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_parent(self, id, new_parent_name, new_parent_surname, new_parent_phone_number = None, new_parent_email = None):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE parent_table SET name = (%s), surname = (%s), phone_number = (%s), email = (%s)
                        WHERE id = (%s) """
            param = (new_parent_name, new_parent_surname, new_parent_phone_number, new_parent_email, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_parent_id(self, parent_name, parent_surname):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM parent_table WHERE
                        (name = (%s) AND surname = (%s)) """
            param = (parent_name, parent_surname)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id