#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

from .base import *
from .group import Group
from .sconfig import SConfig
from .user import User

from logger import log, trace
import common


@trace()
def initMongoDB(app, db):
    db.init_app(app)
    User.register_delete_rule(Group, 'contact', db.NULLIFY)
    Group.register_delete_rule(User, 'group', db.NULLIFY)

    if User.objects.count() == 0:
        log.info('add users')
        admin = User(name='admin', pasd=common.hash('admin'+common.hash('admin' + 'password')), level=0)
        admin.save()
        master = User(name='master', pasd=common.hash('master'+common.hash('master' + 'password')), level=10)
        master.save()
        user = User(name='user', pasd=common.hash('user'+common.hash('user' + 'password')), level=100)
        user.save()

    if SConfig.objects.count() == 0:
        log.info('add sysconfig')
        syconfig = SConfig()
        syconfig.save()

    if Group.objects.count() == 0:
        log.info('add group')
        admin = User.objects(name='admin').first()
        group = Group()
        group.name = 'Group'
        group.contact = admin
        #group.users = [admin]
        group.desc = '这个是测试用的'
        group.save()
        admin.group = group
        admin.save()
