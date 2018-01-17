#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flask
from flask import Flask, flash, redirect, render_template, request, url_for, Blueprint, g

from flask_login import LoginManager, login_user, logout_user
from flask_login import login_required
from flask_login import UserMixin, current_user

from flask_restful import Api, Resource
import json
from flask_mongoengine import DoesNotExist

from logger import log, trace

import model
import common


class User(UserMixin):
    def __init__(self, user):
        self.user = user

    def get_id(self):
        return self.user.name

    def get_auth_token(self):
        return self.name

    def get(uid):
        user = model.User.objects.get(name=uid)
        if user:
            return User(user)
        else:
            return None


app = Blueprint("login", __name__)

api = Api()

login_manager = LoginManager()


@app.record_once
def on_load(state):
    login_manager.init_app(state.app)
    state.app.config['PERMANENT_SESSION_LIFETIME'] = 36000
    with state.app.app_context():
        g.lm = login_manager
    api.init_app(app)


@login_manager.request_loader
def load_user_from_request(request):
    log.info('request_loader invoked')

    # first, try to login using the api_key url arg
    api_key = request.args.get('ak')
    if api_key:
        user = User.get(api_key)
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('ak')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.get(api_key)
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@trace(label=__name__)
def auth_level(level):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            log.debug("[{0}]invoked by [{1}]".format(func.__name__, current_user.user.name))

            if level == 0:
                if not current_user.user.level < 10:
                    log.debug("[{0}]invoked by [{1}] failed, level expected[{2}], got[{3}] ".format(func.__name__, current_user.user.name, level, current_user.user.level))
                    return {'status': 403, 'msg': 'You are not allowed to do this!!!!', 'payload': ''}
            elif level == 10:
                if not current_user.user.level < 100:
                    log.debug("[{0}]invoked by [{1}] failed, level expected[{2}], got[{3}] ".format(func.__name__, current_user.user.name, level, current_user.user.level))
                    return {'status': 403, 'msg': 'You are not allowed to do this!!!!', 'payload': ''}

            return func(*args, **kwargs)
        return handle_args
    return handle_func


@login_manager.unauthorized_handler
def unauthorized():
    return {'status': 404, 'msg': 'You are not logged in!', 'payload': ''}


class UserInfo(Resource):
    @login_required
    def get(self):
        # Every time userinfo get, it should be consider a fresh session.
        request.headers.get('SESID')
        return {'status': 200,
                'msg': 'welcome!',
                'payload': json.loads(str(current_user.user))
                }


class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return {'status': 200, 'msg': 'You are logged out!', 'payload': None}


class Login(Resource):
    @login_required
    def get(self):
        if current_user.is_authenticated:
            return {'status': 200,
                    'msg': 'You already successfully logged in!',
                    'payload': None}

    def post(self):
        status = 0
        msg = ''
        name = request.json['uname']
        pasd = request.json['upass']
        log.debug('upass=[{0}]'.format(pasd))
        try:
            user = model.User.objects.get(name=name, pasd=common.hash(name + pasd))

            if not user:
                return {'status': 501,
                        'msg': 'Invalid credentials',
                        'payload': ''}
            else:
                login_user(User(user))
                msg = 'You were successfully logged in'
                status = 200
        except DoesNotExist:
            return {'status': 501, 'msg': 'Invalid credentials', 'payload': ''}
        return {'status': status,
                'msg': msg,
                'payload': json.loads(str(current_user.user))}


api.add_resource(Login, '/login/', endpoint='login')
api.add_resource(Logout, '/logout/', endpoint='logout')
api.add_resource(UserInfo, '/user/', endpoint='userinfo')

if __name__ == "__main__":
    from flask import Flask
    APP = Flask(__name__)
    from flask_cors import CORS
    CORS(APP)

    @APP.after_request
    def add_header(response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    APP.register_blueprint(app, url_prefix='/api')
    APP.run(debug=True)
    #app.run()
