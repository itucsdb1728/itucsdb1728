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

class SchoolClass:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        try:
            with dbapi.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS school_class_table (
                            id INTEGER PRIMARY KEY SERIAL,
                            class_id INTEGER NOT NULL REFERENCES class_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            school_id INTEGER NOT NULL REFERENCES school_table(id) ON DELETE CASCADE ON UPDATE CASCADE
                            )
                            """
                cursor.execute(query)

                connection.commit()
        except Exception as e:
            print("Hata var")
            logging.error(str(e))
        

