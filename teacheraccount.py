
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

class TeacherAccount:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        #try:
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS teacher_account_table(
                        id SERIAL primary key,
                        teacher_id INTEGER NOT NULL REFERENCES teacher_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                        userName VARCHAR(60) not null,
                        password VARCHAR(60) not null)"""
            cursor.execute(query)
            connection.commit()

    def insert_teacher_account(self):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO teacher_account_table VALUES
                        (DEFAULT, 1, 'crazyboy', '123456boran') """
            
            cursor.execute(query)
            connection.commit()
    