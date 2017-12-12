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
from flask import redirect
from flask import render_template
from attendance import Attendance
from school import School
from teacher import Teacher
from grade import Grade
from session import Session
from parent import Parent
from student import Student
from lesson import Lesson
from studentschool import StudentSchool
from student_class import Student_Class
from schoolclass import SchoolClass
from studentparent import StudentParent
from teacheraccount import TeacherAccount
from teacherschool import TeacherSchool
from schedule import Schedule
from teacheraccount import TeacherAccount 
from classroom import Class
from lesson import Lesson
from session import Session
from grade import Grade


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

@app.route("/login",methods=["POST"])
def login():
    teacher_account = TeacherAccount(dsn=app.config['dsn'])
    donut=teacher_account.login_check(request.form["username"],request.form["password"])
    if donut=="1":
        return render_template('chooseaction.html')
    elif donut=="0":
        return "Wrong username or password"


@app.route('/create_db')
def create_db():
    if session.get('login'):
        school = School(dsn=app.config['dsn'])
        school.init_table()
        #deneme

        lesson = Lesson(dsn=app.config['dsn'])
        lesson.init_table()

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

        classroom = Class(dsn=app.config['dsn'])
        classroom.init_table()
        #class.insert_class("9A",2013)
        #class.delete_class(class.get_class_id("9A",2013))
        #class.insert_class("10A",2013)
        #class.update_class(class.get_class_id("10A",2013),"12C",2015)

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

        #session = Session(dsn=app.config['dsn'])
        #session.init_table()
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

        schoolclass = SchoolClass(dsn=app.config['dsn'])
        schoolclass.init_table()
        #schoolclass.insert_school_class(3,8)
        #schoolclass.delete_school_class(schoolclass.get_school_class_id(3,8))
        #schoolclass.insert_school_class(3,8)
        #schoolclass.update_school_class(schoolclass.get_school_class_id(3,8),5,10)

        student_class = Student_Class(dsn=app.config['dsn'])
        student_class.init_table()
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
        return "Database created"
    else:
        return redirect(url_for('home_page'))




@app.route("/dashboard",methods=["GET"])
def dashboard(key=None):
    if session.get('login'):
        return "session var"
    else:
        return redirect(url_for('home_page'))

@app.route("/dashboard/add_school",methods=["GET","POST"])
def dashboard_add_school():
    if 'school_name' in request.form:
        school_name = request.form['school_name']
        if not school_name=="":
            page = School(dsn = app.config['dsn'])
            return page.insert_school(school_name)
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
    if session.get('login'):
        schedule = Schedule(dsn=app.config['dsn'])
        teacher_id = session['login']
        classes = schedule.get_all_classes(teacher_id)
        return render_template('sinif_ders_secimi.html',classes=classes)
    else:
        return redirect(url_for('home_page'))

@app.route("/selectschedule")
def selectschedule():
    if session.get('login'):
        schedule = Schedule(dsn=app.config['dsn'])
        classroom = Class(dsn=app.config['dsn'])
        lesson = Lesson(dsn=app.config['dsn'])
        teacher_id = session['login']
        schedules = schedule.get_all_schedules_for_teacher(teacher_id)
        schedule_ids=[]
        class_names=[]
        lesson_names=[]
        for a in schedules:
            schedule_ids.append(a[0])
            my_classroom = classroom.get_class(a[1])
            class_names.append(my_classroom[1])
            my_lesson = lesson.get_lesson(a[2])
            lesson_names.append(my_lesson[1])        
        return render_template('schedule_selection.html',zipped = zip(schedule_ids,lesson_names,class_names))
    else:
        return redirect(url_for('home_page'))

@app.route("/attendancelist",methods=["GET","POST"])
def attendance():
    if session.get('login'):
        studentclass = Student_Class(dsn=app.config['dsn'])
        schedule = Schedule(dsn=app.config['dsn'])
        classroom = Class(dsn=app.config['dsn'])
        student = Student(dsn=app.config['dsn'])
        #attendance = Attendance(dsn=app.config['dsn']) 
        sinif=request.form['sinif']
        derssaat = request.form['derssaati']
        session['sinif'] = sinif
        session['derssaat'] = derssaat
        ids = studentclass.get_id_all_students(sinif)
        names = student.get_all_student_of_class(sinif)
        return render_template('attendance.html',zipped = zip(names,ids))
    else:
        return redirect(url_for('home_page'))

@app.route("/attendancerecord",methods=["GET","POST"])
def attendancerecord():
    if session.get('login'):
        studentclassroom = Student_Class(dsn=app.config['dsn'])
        attendance = Attendance(dsn=app.config['dsn'])
        sinif=session['sinif']
        teacher_id = session['login']
        ids = []
        #ids.append(studentclassroom.get_id_all_students(sinif))
        ids=studentclassroom.get_id_all_students(sinif)
        #ids=studentclassroom.get_tuple_id_all_students(sinif)
        #tuple_ids = tuple(ids)
        #print(ids)
        stringvalue=attendance.insert_attendance(ids,sinif)
        return stringvalue
    else:
        return redirect(url_for('home_page'))

@app.route("/gradelist",methods=["GET","POST"])
def gradelist():
    if session.get('login'):
        studentclass = Student_Class(dsn=app.config['dsn'])
        schedule = Schedule(dsn=app.config['dsn'])
        student = Student(dsn=app.config['dsn']) 
        schedule_id=request.form['schedule']
        session['schedule_id'] = schedule_id
        my_schedule = schedule.get_schedule(schedule_id)
        class_id = my_schedule[1]
        students = studentclass.get_classs_all_students(class_id)
        student_ids=[]
        names=[]
        surnames=[]
        for a in students:
            student_ids.append(a[0])
            my_student = student.get_student(a[0])
            names.append(my_student[1])
            surnames.append(my_student[2])
        return render_template('grade.html',zipped = zip(student_ids,names,surnames))
    else:
        return redirect(url_for('home_page'))

@app.route("/graderecord",methods=["GET","POST"])
def graderecord():
    if session.get('login'):
        studentclass = Student_Class(dsn=app.config['dsn'])
        schedule = Schedule(dsn=app.config['dsn'])
        grade = Grade(dsn=app.config['dsn'])
        explanation = request.form['aciklama']
        schedule_id = session['schedule_id']
        my_schedule = schedule.get_schedule(schedule_id)
        class_id = my_schedule[1]
        students = studentclass.get_classs_all_students(class_id)
        for id in students:
            my_grade = request.form[str(id[0])]
            grade.insert_grade(schedule_id,id[0],my_grade,explanation)
        return "basarili!!!"
    else:
        return redirect(url_for('home_page'))


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




        