
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

class TeacherSchool:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS teacherschool_table(
                        id SERIAL primary key,
                        teacher_id INTEGER NOT NULL REFERENCES teacher_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                        school_id INTEGER NOT NULL REFERENCES schools_table(id) ON DELETE CASCADE ON UPDATE CASCADE)"""
            cursor.execute(query)

            connection.commit()

    def insert_teacherschool(self, teacher_id, school_id):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO teacherschool_table VALUES
                        (DEFAULT,(%s),(%s)) """
            param = (teacher_id, school_id)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_teacherschool(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM teacherschool_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_teacherschool(self, id, new_teacher_id, new_school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE teacherschool_table SET teacher_id = (%s), school_id = (%s)
                        WHERE id = (%s) """
            param = (new_teacher_id, new_school_id ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_teacherschool_id(self, teacher_id, school_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM teacherschool_table WHERE
                        (teacher_id = (%s) AND school_id = (%s)) """
            param = (teacher_id, school_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_teachers_school_id(self, teacher_id):

        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT school_id FROM teacherschool_table WHERE
                        (teacher_id = (%s)) """
            param = (teacher_id,)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_schools_all_teachers(self, school_id):
    
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT teacher_id FROM teacherschool_table WHERE
                        (school_id = (%s)) """
            param = (school_id,)
            
            cursor.execute(query,param)

            teachers = cursor.fetchall()
            
            connection.commit()

            return teachers

    def get_teachers_all_schools(self, teacher_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT school_id FROM teacherschool_table WHERE
                        (teacher_id = (%s)) """
            param = (teacher_id,)
            
            cursor.execute(query,param)

            schools = cursor.fetchall()
            
            connection.commit()

            return schools

