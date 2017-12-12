import datetime
import os
import traceback
import logging
import psycopg2 as dbapi2
from flask import render_template
from flask import Flask
from flask import request
from flask import redirect
from flask import session
from flask.helpers import url_for
from classroom import Classroom
from school import School
from teacher import Teacher
from grade import Grade
from session import Session
from parent import Parent
from student import Student
from lesson import Lesson
from studentschool import StudentSchool
from student_classroom import Student_Classroom
from schoolclassroom import SchoolClassroom
from studentparent import StudentParent
from teacheraccount import TeacherAccount
from teacherschool import TeacherSchool
from schedule import Schedule
from teacheraccount import TeacherAccount 

app = Flask(__name__)

class Attendance:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS attendance_table (
                            id SERIAL PRIMARY KEY,
                            student_id INTEGER NOT NULL REFERENCES student_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            teacher_id INTEGER NOT NULL REFERENCES teacher_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            attendance_date DATE NOT NULL,
                            situation BOOLEAN NOT NULL
                            )"""
                cursor.execute(query)

                connection.commit()


    def insert_attendance(self,ids,sinif):
        teacher_id = session['login']
        now = datetime.datetime.now()
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            for id in ids:
                attendance_situation = request.form[str(id)]
                query = """INSERT INTO attendance_table VALUES (DEFAULT,(%s),(%s),(%s),(%s))"""
                param=(id,teacher_id,now,attendance_situation)
                cursor.execute(query,param)
            connection.commit()
        return "yoklama kaydedildi"

    def delete_attendance(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM attendance_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_attendance(self, id, new_student_id, new_session_id, new_situation):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE attendance_table SET student_id = (%s), session_id = (%s), situation = (%s)
                        WHERE id = (%s) """
            param = (new_student_id, new_session_id, new_situation ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_attendance_id(self, student_id, session_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM attendance_table WHERE
                        (student_id = (%s) AND session_id = (%s)) """
            param = (student_id, session_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id





    