
import datetime
import os
import traceback
import logging
import psycopg2 as dbapi2
#import sys
from flask import request
from flask import render_template
from flask import Flask
from flask import session
from flask import redirect
from flask.helpers import url_for
from teacher import Teacher

app = Flask(__name__)

class TeacherAccount:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS teacher_account_table(
                        id SERIAL primary key,
                        teacher_id INTEGER NOT NULL REFERENCES teacher_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                        username VARCHAR(60) UNIQUE not null,
                        password VARCHAR(60) not null)"""
            cursor.execute(query)
            connection.commit()

    def insert_teacher_account(self, teacher_id, username, password):
        
        with dbapi2.connect(self.dsn) as connection:

            cursor = connection.cursor()

            query = """INSERT INTO teacher_account_table VALUES
                        (DEFAULT,(%s),(%s),(%s)) """
            param = (teacher_id, username, password)
            
            
            cursor.execute(query,param)
            connection.commit()

    def delete_teacher_account(self, id):
        
        with dbapi2.connect(self.dsn) as connection:

            cursor = connection.cursor()

            query = """DELETE FROM teacher_account_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_teacher_account(self, id, new_teacher_id, new_username, new_password):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE teacher_account_table SET teacher_id = (%s), username = (%s), password = (%s)
                        WHERE id = (%s) """
            param = (new_teacher_id, new_username, new_password, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_teacher_account_id(self, username):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM teacher_account_table WHERE
                        username = (%s) """
            param = (username)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_teacher_account(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM teacher_account_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)

            teacher_account = cursor.fetchone()
            
            connection.commit()

            return teacher_account

    
    
    

    def login_check(self,username,password):
        with dbapi2.connect(self.dsn)  as connection:
            query="SELECT teacher_id FROM teacher_account_table WHERE username='%s' AND password='%s'" %(username,password)
            cursor=connection.cursor()
            result=cursor.execute(query)
            teacher_id = cursor.fetchone()
            if cursor.rowcount>0:
                session['login'] = teacher_id
                #return redirect(url_for('select_class'))
                return "1"
            else:           
                return "0"
     
        