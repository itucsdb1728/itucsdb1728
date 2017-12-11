
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

class StudentParent:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """CREATE TABLE IF NOT EXISTS studentparent_table(
                        id SERIAL primary key,
                        student_id INTEGER NOT NULL REFERENCES student_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                        parent_id INTEGER NOT NULL REFERENCES parent_table(id) ON DELETE CASCADE ON UPDATE CASCADE)"""
            cursor.execute(query)

            connection.commit()

    def insert_studentparent(self, student_id, parent_id):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO studentparent_table VALUES
                        (DEFAULT,(%s),(%s)) """
            param = (student_id, parent_id)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_studentparent(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM studentparent_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_studentparent(self, id, new_student_id, new_parent_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE studentparent_table SET student_id = (%s), parent_id = (%s)
                        WHERE id = (%s) """
            param = (new_student_id, new_parent_id ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_studentparent_id(self, student_id, parent_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM studentparent_table WHERE
                        (student_id = (%s) AND parent_id = (%s)) """
            param = (student_id, parent_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_students_parent(self, student_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT parent_id FROM studentparent_table WHERE
                        (student_id = (%s)) """
            param = (student_id,)
            
            cursor.execute(query,param)

            parent_id = cursor.fetchone()
            
            connection.commit()

            return parent_id

    def get_parents_student(self, parent_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT student_id FROM studentparent_table WHERE
                        (parent_id = (%s)) """
            param = (parent_id,)
            
            cursor.execute(query,param)

            student_id = cursor.fetchone()
            
            connection.commit()

            return student_id

    def get_parents_all_students(self, parent_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT student_id FROM studentparent_table WHERE
                        (parent_id = (%s)) """
            param = (parent_id,)
            
            cursor.execute(query,param)

            students = cursor.fetchall()
            
            connection.commit()

            return students

    def get_students_all_parents(self, student_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT parent_id FROM studentparent_table WHERE
                        (student_id = (%s)) """
            param = (student_id,)
            
            cursor.execute(query,param)

            parents = cursor.fetchall()
            
            connection.commit()

            return parents