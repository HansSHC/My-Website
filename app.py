from bottle import route, run, template, view, static_file, request, redirect, error
import requests
from datetime import datetime

#Using Bottle.py create an API tp AGIFY.IO

from bottle import run , route, template

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/')
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    return template('homepage', time=current_time)      

@route('/football')
@view('page1')
def sport():
    pass
#main routine
run(host='0.0.0.0', port=4000, reloader=True, debug=True)
