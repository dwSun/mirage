#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flask
from flask import Flask, flash, redirect, render_template, request, url_for, Blueprint,g

from flask_login import login_required,current_user
from flask_mongoengine import DoesNotExist

from flask_restful import Api, Resource
import json
import model
from logger import log, trace

app = Blueprint("sysconfig", __name__)
api = Api()


@app.record_once
def on_load(state):
    api.init_app(app)


class SConfig(Resource):
    @login_required
    def get(self):
        log.info(request.headers.get('SESID'))
        sysconfig = model.SConfig.objects.exclude('id').first()
        dit = sysconfig.toDict()
        return {'status': 200, 'msg': '', 'payload': dit}

    @login_required
    def post(self):
        data = request.json
        sysconfig = model.SConfig.objects.first()
        sysconfig.pitems = data['pitems']
        sysconfig.save()

        return {'status': 200, 'msg': '', 'payload': sysconfig.toDict()}


api.add_resource(SConfig, '/sysconfig/', endpoint='sysconfig')
