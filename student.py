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
                        email VARCHAR(30)
                        )
                        """
            cursor.execute(query)
            connection.commit()

    def add_student(self, name, surname, branch, ismanager):        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO teacher_table VALUES
                        (DEFAULT,(%s),(%s),(%s),(%s)) """
            param = (name, surname, branch ,ismanager)            
            cursor.execute(query,param)
            connection.commit()
        return redirect(url_for('dashboard_add_teacher'))    