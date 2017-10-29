import datetime
import os
import traceback
import logging
import psycopg2 as dbapi
from flask import Flask
from flask import render_template
from schools import Schools

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
dsn = """user='root' password='123' host='localhost' port=5000
              dbname='db_yoklama'"""


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/create_db')
def create_db():
    try:
        now = datetime.datetime.now()
        school = Schools(dsn=dsn)
        school.init_table()
        return render_template('home.html', current_time=now.ctime())
    except Exception as e:
        logging.error(str(e))


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='0.0.0.0', port=port, debug=debug)
