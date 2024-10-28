from bottle import route, run, template, view, static_file, request, redirect, error
import requests

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/')
def index():

    return template('homepage')      

@route('/football')
@view('page1')
def sport():
    pass
#main routine
run(host='0.0.0.0', port=4000, reloader=True, debug=True)
