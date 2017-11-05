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

class Attendance:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        try:
            with dbapi.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS attendance_table (
                            id INTEGER PRIMARY KEY SERIAL,
                            student_id INTEGER NOT NULL REFERENCES student_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            session_id INTEGER NOT NULL REFERENCES session_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            situation BOOLEAN NOT NULL
                            )
                            """
                cursor.execute(query)

                connection.commit()
        except Exception as e:
            print("Hata var")
            logging.error(str(e))