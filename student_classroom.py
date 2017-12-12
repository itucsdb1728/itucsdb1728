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

class Student_Classroom:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS student_classroom_table (
                            id SERIAL PRIMARY KEY,
                            classroom_id INTEGER NOT NULL REFERENCES classroom_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            student_id INTEGER NOT NULL REFERENCES student_table(id) ON DELETE CASCADE ON UPDATE CASCADE
                            )
                            """
                cursor.execute(query)

                connection.commit()

    def insert_student_classroom(self, classroom_id, student_id):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO student_classroom_table VALUES
                        (DEFAULT,(%s),(%s)) """
            param = (classroom_id, student_id)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_student_classroom(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM student_classroom_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_student_classroom(self, id, new_classroom_id, new_student_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE student_classroom_table SET classroom_id = (%s), student_id = (%s)
                        WHERE id = (%s) """
            param = (new_classroom_id, new_student_id ,id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_student_classroom_id(self, classroom_id, student_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM student_classroom_table WHERE
                        (classroom_id = (%s) AND student_id = (%s)) """
            param = (classroom_id, student_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_students_classroom(self, student_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT classroom_id FROM student_classroom_table WHERE
                        (student_id = (%s)) """
            param = (student_id,)
            
            cursor.execute(query,param)

            classroom_id = cursor.fetchone()
            
            connection.commit()

            return classroom_id
        
    def get_classrooms_all_students(self, classroom_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT student_id FROM student_class_table WHERE
                        (class_id = (%s)) """
            param = (classroom_id,)
            
            cursor.execute(query,param)

            data = cursor.fetchall()

            dataList=[]

            for a in data:
                dataList.append(a[0])
            return dataList


    def get_id_all_students(self, classroom_name):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT student_id FROM student_class_table WHERE
                        class_id IN (SELECT id FROM class_table WHERE name =(%s)) """
            param = (classroom_name,)
            
            cursor.execute(query,param)

            data = cursor.fetchall()

            dataList=[]

            for a in data:
                dataList.append(a[0])
            return dataList


    def get_tuple_id_all_students(self, classroom_name):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT student_id FROM student_class_table WHERE
                        class_id IN (SELECT id FROM class_table WHERE name =(%s)) """
            param = (classroom_name,)
            
            cursor.execute(query,param)

            data = cursor.fetchall()

            return data


