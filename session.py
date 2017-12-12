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

class Session:
    def __init__(self,dsn):
        self.dsn = dsn
        return

    def init_table(self):
            with dbapi2.connect(self.dsn) as connection: 

                cursor = connection.cursor()
                query = """CREATE TABLE IF NOT EXISTS session_table (
                            id SERIAL PRIMARY KEY,
                            schedule_id INTEGER NOT NULL REFERENCES schedule_table(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            session_date DATE NOT NULL,
                            row INTEGER NOT NULL CHECK (row >= 1 AND row <= 10)
                            )
                            """
                cursor.execute(query)

                connection.commit()

    def insert_session(self, schedule_id, session_date, row):
            
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO session_table VALUES
                        (DEFAULT,(%s),(%s),(%s)) """
            param = (schedule_id, session_date, row)
            
            cursor.execute(query,param)
            connection.commit()

    def delete_session(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM session_table WHERE
                        (id = (%s)) """
            param = (id)
            
            cursor.execute(query,param)
            connection.commit()

    def update_session(self, id, new_schedule_id, new_session_date, new_row):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """UPDATE session_table SET schedule_id = (%s), session_date = (%s), row = (%s)
                        WHERE id = (%s) """
            param = (new_schedule_id, new_session_date, new_row, id)
            
            cursor.execute(query,param)
            connection.commit()

    def get_session_id(self, schedule_id, session_date, row):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT id FROM session_table WHERE
                        (schedule_id = (%s) AND session_date = (%s) AND row = (%s)) """
            param = (schedule_id, session_date, row)
            
            cursor.execute(query,param)

            id = cursor.fetchone()
            
            connection.commit()

            return id

    def get_session(self, id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM session_table WHERE
                        (id = (%s)) """
            param = (id,)
            
            cursor.execute(query,param)

            session = cursor.fetchone()
            
            connection.commit()

            return session

    def get_all_sessions_for_schedule(self, schedule_id):
        
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM session_table WHERE
                        (schedule_id = (%s)) """
            param = (schedule_id,)
            
            cursor.execute(query,param)

            sessions = cursor.fetchall()
            
            connection.commit()

            return sessions