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
from flask import Flask
from flask import render_template
from school import School
from teacher import Teacher
from parent import Parent
from student import Student
from studentschool import StudentSchool
from student_classroom import Student_Classroom
from schoolclassroom import SchoolClassroom
from studentparent import StudentParent
from teacheraccount import TeacherAccount
from teacherschool import TeacherSchool
from attendance import Attendance
from schedule import Schedule
from teacheraccount import TeacherAccount 
from classroom import Classroom
from lesson import Lesson
from session import Session
from grade import Grade
#from schoolclass import School_Class


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
    #deneme

    teacher = Teacher(dsn=app.config['dsn'])
    teacher.init_table()
    
    parent = Parent(dsn=app.config['dsn'])
    parent.init_table()

    teacher_account = TeacherAccount(dsn=app.config['dsn'])
    teacher_account.init_table()

    student = Student(dsn=app.config['dsn'])
    student.init_table()
    #student.insert_student("Boran","Sivrikaya","hotmail")
    #student.delete_student(student.get_student_id("Boran","Sivrikaya"))
    #student.insert_student("Boran","Sivrikaya","hotmail")
    #student.update_student(student.get_student_id("Boran","Sivrikaya"),"Hamza","Tuna","gmail")

    school = School(dsn=app.config['dsn'])
    school.init_table()
    #school.insert_school("Makif")
    #school.delete_school(school.get_school_id("Makif"))
    #school.insert_school("GOP")
    #school.update_school(school.get_school_id("GOP"),"IAFL")

    classroom = Classroom(dsn=app.config['dsn'])
    classroom.init_table()
    #classroom.insert_classroom("9A",2013)
    #classroom.delete_classroom(classroom.get_classroom_id("9A",2013))
    #classroom.insert_classroom("10A",2013)
    #classroom.update_classroom(classroom.get_classroom_id("10A",2013),"12C",2015)

    lesson = Lesson(dsn=app.config['dsn'])
    lesson.init_table()
    #lesson.insert_lesson("Math")
    #lesson.delete_lesson(lesson.get_lesson_id("Math"))
    #lesson.insert_lesson("History")
    #lesson.update_lesson(lesson.get_lesson_id("History"),"Science")

    parent = Parent(dsn=app.config['dsn'])
    parent.init_table()
    #parent.insert_parent("Zekiye","Sivrikaya")
    #parent.delete_parent(parent.get_parent_id("Zekiye","Sivrikaya"))
    #parent.insert_parent("Hamdi","Sivrikaya")
    #parent.update_parent(parent.get_parent_id("Hamdi","Sivrikaya"),"Ahmet","Yalcin")

    schedule = Schedule(dsn=app.config['dsn'])
    schedule.init_table()
    #schedule.insert_schedule(5,4,6,2013)
    #schedule.delete_schedule(schedule.get_schedule_id(5,4))
    #schedule.insert_schedule(5,4,6,2013)
    #schedule.update_schedule(schedule.get_schedule_id(5,4),3,4,6,2020)

    session = Session(dsn=app.config['dsn'])
    session.init_table()
    #session.insert_session(3,"2-2-1922",3)
    #session.delete_session(session.get_session_id(3,"2-2-1922",3))
    #session.insert_session(3,"2-2-1922",7)
    #session.update_session(session.get_session_id(3,"2-2-1922",7),4,"8-8-1994",1)

    attendance = Attendance(dsn=app.config['dsn'])
    attendance.init_table()
    #attendance.insert_attendance(2,4,True)
    #attendance.delete_attendance(attendance.get_attendance_id(2,4))
    #attendance.insert_attendance(2,5,True)
    #attendance.update_attendance(attendance.get_attendance_id(2,5),4,6,False)

    grade = Grade(dsn=app.config['dsn'])
    grade.init_table()
    #grade.insert_grade(3,2,75,"Iyi not")
    #grade.delete_grade(grade.get_grade_id(3,2))
    #grade.insert_grade(3,2,85,"Daha iyi")
    #grade.update_grade(grade.get_grade_id(3,2),4,4,20,"VF")

    schoolclassroom = SchoolClassroom(dsn=app.config['dsn'])
    schoolclassroom.init_table()
    #schoolclass.insert_school_class(3,8)
    #schoolclass.delete_school_class(schoolclass.get_school_class_id(3,8))
    #schoolclass.insert_school_class(3,8)
    #schoolclass.update_school_class(schoolclass.get_school_class_id(3,8),5,10)

    student_classroom = Student_Classroom(dsn=app.config['dsn'])
    student_classroom.init_table()
    #student_class.insert_student_class(3,2)
    #student_class.delete_student_class(student_class.get_student_class_id(3,2))
    #student_class.insert_student_class(5,2)
    #student_class.update_student_class(student_class.get_student_class_id(5,2),7,4)

    studentparent = StudentParent(dsn=app.config['dsn'])
    studentparent.init_table()
    #studentparent.insert_studentparent(2,2)
    #studentparent.delete_studentparent(studentparent.get_studentparent_id(2,2))
    #studentparent.insert_studentparent(2,2)
    #studentparent.update_studentparent(studentparent.get_studentparent_id(2,2),4,2)

    studentschool = StudentSchool(dsn=app.config['dsn'])
    studentschool.init_table()
    #studentschool.insert_studentschool(2,8)
    #studentschool.delete_studentschool(studentschool.get_studentschool_id(2,8))
    #studentschool.insert_studentschool(4,10)
    #studentschool.update_studentschool(studentschool.get_studentschool_id(4,10),4,12)

    teacherschool = TeacherSchool(dsn=app.config['dsn'])
    teacherschool.init_table()
    #teacherschool.insert_teacherschool(2,8)
    #teacherschool.delete_teacherschool(teacherschool.get_teacherschool_id(2,8))
    #teacherschool.insert_teacherschool(4,10)
    #teacherschool.update_teacherschool(teacherschool.get_teacherschool_id(4,10),6,12)


    return "YAZDIKK"

@app.route('/test')
def test():
    teacher = Teacher(dsn=app.config['dsn'])
    my_teacher = teacher.get_teacher(teacher.get_teacher_id("Yalcin","Sahin"))
    print(my_teacher[2])
    return "testtt"
    
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
