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

class Classes:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        with dbapi.connect(self.dsn) as connection: 

            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS class_table (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(7) NOT NULL,
                        year INTEGER NOT NULL CHECK (year >= 2012 AND year<=2053)
                        )
                        """
            cursor.execute(query)
            connection.commit()
        

