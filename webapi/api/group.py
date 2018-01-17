#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flask
from flask import Flask, flash, redirect, render_template, request, url_for, Blueprint,g

from flask_login import login_required, current_user
from flask_mongoengine import DoesNotExist
from mongoengine import ValidationError
from mongoengine import errors

from flask_restful import Api, Resource
import json
import model

from login import auth_level

from logger import log, trace

app = Blueprint("group", __name__)

api = Api()

@app.record_once
def on_load(state):
    api.init_app(app)


class Group(Resource):
    @login_required
    @auth_level(0)
    def get(self, id=None):
        if id:
            try:
                group = model.Group.objects.get(id=id)
                dit = group.toDict()
                dit['id'] = str(group.id)
                if group.contact:
                    dit['contact'] = str(group.contact.name)
                return {'status': 200, 'msg': '', 'payload': dit}
            except DoesNotExist:
                return {'status': 404,
                        'msg': 'Group with [{0}] not found!'.format(id),
                        'payload': {}}
            except ValidationError:
                try:
                    group = model.Group.objects.get(name=id)
                    dit = group.toDict()
                    dit['id'] = str(group.id)
                    if group.contact:
                        dit['contact'] = str(group.contact.name)
                    return {'status': 200,
                            'msg': '',
                            'payload': dit}
                except DoesNotExist:
                    return {'status': 404,
                            'msg': 'Group with [{0}] not found!'.format(id),
                            'payload': {}}

        else:
            groups = []
            for group in  model.Group.objects:
                groups.append({'id': str(group.id),
                               'name': group.name,
                               'desc': group.desc,
                               'users': model.User.objects(group=group).all().count()})
            return {'status': 200,
                    'msg': '',
                    'payload': groups}

    @login_required
    @auth_level(0)
    def post(self, id=None):
        data = request.json
        groupID = id if id else data['id']
        try:
            group = model.Group.objects.get(id=id)
            if not group:
                return {'status': 404,
                        'msg': 'Group with [{0}] not found!'.format(name),
                        'payload': {}}
            else:
                self.setGroup(group, data)

                return {'status': 200,
                        'msg': '',
                        'payload': group.toDict()}
        except DoesNotExist:
            return {'status': 404,
                    'msg': 'Group with [{0}] not found!'.format(id),
                    'payload': {}}

    def setGroup(self, group, data):
        group.name = data['name']
        group.desc = data['desc']

        if data['contact']:
            group.contact = model.User.objects.get(name=data['contact'])
        group.save()

    @login_required
    @auth_level(0)
    def put(self, id=None):
        if id:
            log.info(id)

        data = request.json

        try:
            group = model.Group.objects.exclude('id').get(name=data['name'])
            return {'status': 403, 'msg': '组名重复', 'payload': None}
        except DoesNotExist:
            pass

        group = model.Group()
        self.setGroup(group, data)

        return {'status': 200,
                'msg': '',
                'payload': group.toDict()}

    @login_required
    @auth_level(0)
    def delete(self, id=None):
        if not id:
            return {'status': 403,
                    'msg': 'not allowed',
                    'payload': {'id': id}}

        try:
            group = model.Group.objects.get(id=id)
            if not group:
                return {'status': 404,
                        'msg': 'Group with [{0}] not found!'.format(name),
                        'payload': {}}
            else:
                group.delete()

                return {'status': 200,
                        'msg': '',
                        'payload': group.toDict()}
        except DoesNotExist:
            return {'status': 404,
                    'msg': 'Group with [{0}] not found!'.format(id),
                    'payload': {}}
        except errors.OperationError:
            return {'status': 409,
                    'msg': 'Delete Failed, please check exist reference.',
                    'payload': {}}


api.add_resource(Group, '/group/', '/group/<string:id>/', endpoint='group')
