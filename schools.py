
import datetime
import os
import traceback
import logging
import psycopg2 as dbapi
from flask import render_template
from flask import Flask
from flask import redirect
from flask.helpers import url_for

app = Flask(__name__)

class Schools:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        try:
            with dbapi.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE schools_table (
                            id integer PRIMARY KEY,
                            school_name text NOT NULL)
                            """
                cursor.execute(query)


                # query = """INSERT INTO schools_table (school_name)
                #             VALUES
                #             ('mehmet akif');"""
                # cursor.execute(query)

                connection.commit()
        except Exception as e:
            print("Hata var")
            logging.error(str(e))
        #return redirect(url_for('/'))

    def add_school(self,school_name):
        with dbapi.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO schools_table (school_name) VALUES ('%s')"""%(school_name)