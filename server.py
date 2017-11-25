import datetime
import json
import os
import re
import traceback
import logging
import psycopg2 as dbapi2
#import sys
from flask import Flask
from flask import render_template
from school import School
from teacher import Teacher
from parent import Parent
from teacheraccount import TeacherAccount 

app = Flask(__name__)


def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    #deneme
    return render_template('home.html', current_time=now.ctime())

@app.route('/create_db')
def create_db():

    school = School(dsn=app.config['dsn'])
    school.init_table()
    #deneme

    teacher = Teacher(dsn=app.config['dsn'])
    teacher.init_table()
    teacher.insert_teacher('Boran','Sivrikaya','Math',False)

    parent = Parent(dsn=app.config['dsn'])
    parent.init_table()

    teacher_account = TeacherAccount(dsn=app.config['dsn'])
    teacher_account.init_table()
    teacher_account.insert_teacher_account('Boran','Sivrikaya','crazyboy','123456boran')
    return "YAZDIKK" 



if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port,debug = 5000,True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='root' password='123' host='localhost' port=5432 dbname='db_yoklama'"""

    app.run(host='0.0.0.0',port=port,debug=debug)
