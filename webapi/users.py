#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flask
from flask import Flask, flash, redirect, render_template, request, url_for, Blueprint,g

from flask_login import login_required, current_user
from flask_mongoengine import DoesNotExist

from flask_restful import Api, Resource
import json
import model

from logger import log, trace
import wicket

app = Blueprint("users", __name__)
api = Api()


@app.record_once
def on_load(state):
    api.init_app(app)


class User(Resource):
    @login_required
    def get(self, name=None):
        if name:
            user = wicket.user.get(name)
            if user:
                return {'status': 200, 'msg': '', 'payload': user}
            else:
                return {'status': 404, 'msg': 'User with [{0}] not found!'.format(name), 'payload': {}}
        else:
            return {'status': 200, 'msg': '', 'payload': wicket.user.get()}

    @login_required
    def post(self, name=None):
        data = request.json
        return {'status': 200, 'msg': '', 'payload': wicket.user.update(data)}

    @login_required
    def put(self):
        data = request.json
        wicket.user.add(data)
        return {'status': 200, 'msg': '', 'payload': {}}

    @login_required
    def delete(self, name=None):
        if not name:
            return {'status': 403, 'msg': 'not allowed', 'payload': {'id': name}}

        try:
            user = model.User.objects.get(name=name)
            if not user:
                return {'status': 404,
                        'msg': 'User with [{0}] not found!'.format(name),
                        'payload': {}}
            else:
                user.delete()

                return {'status': 200, 'msg': '', 'payload': user.toDict()}
        except DoesNotExist:
            return {'status': 404,
                    'msg': 'User with [{0}] not found!'.format(name),
                    'payload': {}}


api.add_resource(User, '/users/', '/users/<string:name>/', endpoint='users')
