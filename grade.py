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

class Grade:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        try:
            with dbapi.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS grade_table (
                            id INTEGER PRIMARY KEY SERIAL,
                            schedule_id INTEGER NOT NULL REFERENCES schedule_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            student_id INTEGER NOT NULL REFERENCES student_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            grade INTEGER NOT NULL CHECK(grade >= 0 AND grade <= 100),
                            # burada hata olabilir
                            explanation TEXT
                            # 1. sınav 2. sınav 2.sözlü vesaire...
                            )
                            """
                cursor.execute(query)

                connection.commit()
        except Exception as e:
            print("Hata var")
            logging.error(str(e))