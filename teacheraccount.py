
import datetime
import os
import traceback
import logging
import psycopg2 as dbapi2
#import sys
from flask import request
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

    def insert_teacher_account(self, name, surname, username, password):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()

            query = """SELECT id FROM teacher_table WHERE(name = (%s) AND surname = (%s))"""
            param = (name, surname)

            cursor.execute(query,param)
            teacher_id = cursor.fetchall()

            print(teacher_id);

            
            query = """INSERT INTO teacher_account_table VALUES
                        (DEFAULT,(%s),(%s),(%s)) """
            param = (teacher_id[0], username, password)
            
            
            cursor.execute(query,param)
            connection.commit()

    def login_check(self,username,password):
        with dbapi2.connect(self.dsn)  as connection:
            query="SELECT * FROM teacher_account_table WHERE username='%s' AND password='%s'" %(username,password)
            cursor=connection.cursor()
            cursor.execute(query)
            is_exist=cursor.fetchall()
            if is_exist is None:
                return "wrong username or password"
            else:
                return "WELCOME!"
        