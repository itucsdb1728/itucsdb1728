
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
            connection.commit()

    def add_school(self,school_name):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO schools_table VALUES (DEFAULT,('%s')) """%(school_name)
            cursor.execute(query)
            connection.commit()
        return redirect(url_for('dashboard_add_school'))