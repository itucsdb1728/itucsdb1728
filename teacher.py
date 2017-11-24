
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
    def insert_teacher(self):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO teacher_table VALUES
                        (DEFAULT,'Boran', 'Sivrikaya', 'Math', TRUE) """
            
            cursor.execute(query)
            connection.commit()
    