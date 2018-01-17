#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
from gevent.pywsgi import WSGIServer

from flask import Flask
from flask_cors import CORS
import json


import model
# apis
from login import app as login
from users import app as users
import api
from logger import Logger

l = Logger(logpath='webapi.log', logname='webapi')
trace = l.trace
log = l.getlog()

app = Flask('webapi')

CORS(app)


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


log.debug('reg all api ...')
app.register_blueprint(login, url_prefix='/api')
app.register_blueprint(users, url_prefix='/api')
app.register_blueprint(api.group, url_prefix='/api')
app.register_blueprint(api.sconfig, url_prefix='/api')
log.debug('reg all api done ...')

log.debug('mongodb initial ...')
app.config['MONGODB_DB'] = 'mirage'
app.config['MONGODB_HOST'] = "127.0.0.1"
app.config['MONGODB_PORT'] = 27017
app.secret_key = 'some_secret'
model.initMongoDB(app, model.db)
log.debug('mongodb initial done...')


if __name__ == '__main__':
    log.info('running...')
    app.run(debug=True, host='0.0.0.0')

    #http = WSGIServer(('', 5000), app)
    #http.serve_forever()
