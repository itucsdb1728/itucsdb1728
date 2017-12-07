
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

class StudentSchool:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS studentschool_table(
                        id SERIAL primary key,
                        student_id INTEGER NOT NULL REFERENCES student_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                        school_id INTEGER NOT NULL REFERENCES schools_table(id) ON DELETE CASCADE ON UPDATE CASCADE)"""
            cursor.execute(query)
            
            connection.commit()

    def insert_studentschool(self, student_id, school_id):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO studentschool_table VALUES
                        (DEFAULT,(%s),(%s)) """
            param = (student_id, school_id)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_studentschool(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM studentschool_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_studentschool(self, id, new_student_id, new_school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE studentschool_table SET student_id = (%s), school_id = (%s)
                        WHERE id = (%s) """
            param = (new_student_id, new_school_id ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_studentschool_id(self, student_id, school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM studentschool_table WHERE
                        (student_id = (%s) AND school_id = (%s)) """
            param = (student_id, school_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id