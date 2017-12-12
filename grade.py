import datetime
import os
import traceback
import logging
import psycopg2 as dbapi2
from flask import render_template
from flask import Flask
from flask import redirect
from flask.helpers import url_for

app = Flask(__name__)

class Grade:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS grade_table (
                            id SERIAL PRIMARY KEY,
                            schedule_id INTEGER NOT NULL REFERENCES schedule_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            student_id INTEGER NOT NULL REFERENCES student_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            grade INTEGER NOT NULL CHECK(grade >= 0 AND grade <= 100),
                            explanation varchar(25) NOT NULL,
                            UNIQUE (schedule_id,explanation)
                            )
                            """
                cursor.execute(query)

                connection.commit()

    def insert_grade(self, schedule_id, student_id, grade, explanation):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO grade_table VALUES
                        (DEFAULT,(%s),(%s),(%s),(%s)) """
            param = (schedule_id, student_id, grade, explanation)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_grade(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM grade_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)
            connection.commit()

    def update_grade(self, id, new_schedule_id, new_student_id, new_grade, new_explanation):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE grade_table SET schedule_id = (%s), student_id = (%s), grade = (%s), explanation = (%s)
                        WHERE id = (%s) """
            param = (new_schedule_id, new_student_id, new_grade, new_explanation ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_grade_id(self, schedule_id, student_id, explanation):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM grade_table WHERE
                        (schedule_id = (%s) AND student_id = (%s) AND explanation = (%s)) """
            param = (schedule_id, student_id, explanation)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_grade(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM grade_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)

            grade = cursor.fetchone()
            
            connection.commit()

            return grade

    def get_all_grades_for_student(self, student_id):
    
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM grade_table WHERE
                        (student_id = (%s)) """
            param = (student_id,)
            
            cursor.execute(query,param)

            grades = cursor.fetchall()
            
            connection.commit()

            return grades

    def get_all_grades_for_schedule(self, schedule_id):

        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM grade_table WHERE
                        (schedule_id = (%s)) """
            param = (schedule_id,)
            
            cursor.execute(query,param)

            grades = cursor.fetchall()
            
            connection.commit()

            return grades
        