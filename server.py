import datetime
import json
import os
import re
import traceback
import logging
import psycopg2 as dbapi2
#import sys
from flask.helpers import url_for
from flask import request
from flask import session
from flask import Flask
from flask import render_template
from school import School
from classes import Classes
from teacher import Teacher
from parent import Parent
from student import Student
from lesson import Lesson
from studentschool import StudentSchool
from studentclass import StudentClass
from schoolclass import SchoolClass
from studentparent import StudentParent
from teacheraccount import TeacherAccount
from teacherschool import TeacherSchool
from attendance import Attendance
from schedule import Schedule
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
    return render_template('login.html')


@app.route('/create_db')
def create_db():

    school = School(dsn=app.config['dsn'])
    school.init_table()
    
    student = Student(dsn=app.config['dsn'])
    student.init_table()

    lesson = Lesson(dsn=app.config['dsn'])
    lesson.init_table()

    teacher = Teacher(dsn=app.config['dsn'])
    teacher.init_table()
    #teacher.insert_teacher('Hamza','Tuna','Science',True)

    classes = Classes(dsn=app.config['dsn'])
    classes.init_table()

    teacher_account = TeacherAccount(dsn=app.config['dsn'])
    teacher_account.init_table()
    #teacher_account.insert_teacher_account('Boran','Sivrikaya','crazyboy','123456boran')

    parent = Parent(dsn=app.config['dsn'])
    parent.init_table()


    school_class = SchoolClass(dsn=app.config['dsn'])
    school_class.init_table()


    teacher_school = TeacherSchool(dsn=app.config['dsn'])
    teacher_school.init_table()

    student_school = StudentSchool(dsn=app.config['dsn'])
    student_school.init_table()

    student_parent = StudentParent(dsn=app.config['dsn'])
    student_parent.init_table()

    student_class = StudentClass(dsn=app.config['dsn'])
    student_class.init_table()

    schedule = Schedule(dsn=app.config['dsn'])
    schedule.init_table()

    attendence = Attendance(dsn=app.config['dsn'])
    attendence.init_table()

    return "YAZDIKK" 
    
@app.route("/login",methods=["POST"])
def login():
    teacher_account = TeacherAccount(dsn=app.config['dsn'])
    yazdir=teacher_account.login_check(request.form["username"],request.form["password"])
    return yazdir

@app.route("/dashboard",methods=["GET"])
def dashboard(key=None):
    if key is None:
        return render_template('dashboard.html')
    else:
        return "DONNNN   "

@app.route("/dashboard/add_school",methods=["GET","POST"])
def dashboard_add_school():
    if 'school_name' in request.form:
        school_name = request.form['school_name']
        if not school_name=="":
            page = School(dsn = app.config['dsn'])
            return page.add_school(school_name)
        else:
            return "bos"
    else: 
        return render_template('dashboard_add_school.html')

@app.route("/dashboard/add_class")
def dashboard_add_class():
    return "add class"

@app.route("/dashboard/add_teacher")
def dashboard_add_teacher():
    return "add teacher"

@app.route("/dashboard/add_student")
def dashboard_add_student():
    return "add student"

@app.route("/dashboard/add_parent")
def dashboard_add_parent():
    return "add parent"

@app.route("/selectclass")
def select_class():
    schedule = Schedule(dsn=app.config['dsn'])
    classes = schedule.select_classes()
    return render_template('sinif_ders_secimi.html',classes=classes)


    return redirect(url_for('history'))

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    app.secret_key = 'super_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
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
