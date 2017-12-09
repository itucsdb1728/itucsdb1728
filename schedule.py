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

class Schedule:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS schedule_table (
                            id SERIAL PRIMARY KEY ,
                            class_id INTEGER NOT NULL REFERENCES classroom_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            lesson_id INTEGER NOT NULL REFERENCES lesson_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            teacher_id INTEGER NOT NULL REFERENCES teacher_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            year INTEGER NOT NULL CHECK (year >= 2012 AND year<=2053)
                            )
                            """
                cursor.execute(query)

                connection.commit()
    
    def insert_schedule(self, class_id, lesson_id, teacher_id, year):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO schedule_table VALUES
                        (DEFAULT,(%s),(%s),(%s),(%s)) """
            param = (class_id, lesson_id, teacher_id, year)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_schedule(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM schedule_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_schedule(self, id, new_class_id, new_lesson_id, new_teacher_id, new_year):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE schedule_table SET class_id = (%s), lesson_id = (%s), teacher_id = (%s), year = (%s)
                        WHERE id = (%s) """
            param = (new_class_id, new_lesson_id, new_teacher_id, new_year, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_schedule_id(self, class_id, lesson_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM schedule_table WHERE
                        (class_id = (%s) AND lesson_id = (%s)) """
            param = (class_id, lesson_id)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id
