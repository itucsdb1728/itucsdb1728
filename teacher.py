
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

class Teacher:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        #try:
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS teacher_table(
                        id SERIAL primary key,
                        name VARCHAR(60) not null,
                        surname VARCHAR(60) not null,
                        branch VARCHAR(40),
                        isManager BOOLEAN not null)"""
            
            connection.commit()
            cursor.execute(query)
<<<<<<< HEAD
    
    def insert_teacher(self, name, surname, branch, ismanager):
        
=======
    def add_teacher(self, name, surname, branch, ismanager):        
>>>>>>> 7821c5b139acab231b0b0ceaf061040e9c0d9be8
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO teacher_table VALUES
                        (DEFAULT,(%s),(%s),(%s),(%s)) """
            param = (name, surname, branch ,ismanager)            
            cursor.execute(query,param)
            connection.commit()
<<<<<<< HEAD

    def delete_teacher(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM teacher_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_teacher(self, id, new_name, new_surname, new_branch, new_ismanager):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE teacher_table SET name = (%s), surname = (%s), branch = (%s), ismanager = (%s)
                        WHERE id = (%s) """
            param = (new_name, new_surname, new_branch ,new_ismanager, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_teacher_id(self, name, surname):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM teacher_table WHERE
                        (name = (%s) AND surname = (%s)) """
            param = (name, surname)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id


=======
        return redirect(url_for('dashboard_add_teacher'))
>>>>>>> 7821c5b139acab231b0b0ceaf061040e9c0d9be8
    