import datetime
import os
import traceback
import logging
import psycopg2 as dbapi2
#import sys
from flask import Flask
from flask import render_template
from school import School
from teacher import Teacher
from parent import Parent
app = Flask(__name__)


# def get_elephantsql_dsn(vcap_services):
#     """Returns the data source name for ElephantSQL."""
#     parsed = json.loads(vcap_services)
#     uri = parsed["elephantsql"][0]["credentials"]["uri"]
#     match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
#     user, password, host, _, port, dbname = match.groups()
#     dsn = """user='{}' password='{}' host='{}' port={}
#              dbname='{}'""".format(user, password, host, port, dbname)
#     return dsn

#for local
<<<<<<< HEAD
dsn = """user='root' password='123' host='localhost' port=5432 dbname='db_yoklama'"""
=======
dsn = """user='root' password='123' host='localhost' port=5432
              dbname='db_yoklama'"""
>>>>>>> 75f8ea508c057e8341d77e3bb6270fbaf24697d2


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/create_db')
def create_db():
<<<<<<< HEAD
    #now = datetime.datetime.now()
    school = School(dsn=dsn)
    school.init_table()

    teacher = Teacher(dsn=dsn)
    teacher.init_table()

    parent = Parent(dsn=dsn)
    parent.init_table()
    #return render_template('home.html', current_time=now.ctime())
    return "YAZDIKK"
=======
    try:
        now = datetime.datetime.now()
        school = Schools(dsn=dsn)
        school.init_table()
        return "Deneme donusu"
    except Exception as e:
        print("server_py hatasi")
        logging.error(str(e))
>>>>>>> 75f8ea508c057e8341d77e3bb6270fbaf24697d2


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='localhost', port=port, debug=debug)
