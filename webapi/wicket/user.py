#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_mongoengine import DoesNotExist
from flask_login import current_user

import model

from logger import trace
import common


def convertUser(user):
    dit = user.toDict()
    if dit['phones']:
        dit['phone'] = dit['phones'][0]

    if user.group:
        dit['group'] = str(user.group.id)
    dit['pasd'] = ''
    return dit


def convert_users(users):
    us = []
    for user in users:
        us.append({'name': user.name,
                   'formalname': user.formalname,
                   'desc': user.desc,
                   'level': user.level,
                   'group': str(user.group.id) if user.group else None,
                   'groupname': user.group.name if user.group else None})
    return us


@trace(__name__)
def get(name=None):
    if current_user.user.level < 10:
        if name:
            dit = None
            try:
                user = model.User.objects.exclude('id').get(name=name)
                dit = convertUser(user)
            except DoesNotExist:
                pass

            return dit
        else:
            return convert_users(model.User.objects)
    else:
        if name:
            dit = None
            try:
                user = model.User.objects.exclude('id').get(name=name, group=current_user.user.group)
                dit = convertUser(user)
            except DoesNotExist:
                pass

            return dit
        else:
            return convert_users(model.User.objects.filter(group=current_user.user.group))


@trace(__name__)
def add(data):
    user = model.User()
    user.name = data['name']
    user.pasd = common.hash(user.name + data['pasd'])
    user.level = int(data['level'])
    user.formalname = data['formalname']
    user.phones = []
    user.phones.append(data['phone'])
    user.address = data['address']
    user.gender = data['gender']
    user.email = data['email']
    user.desc = data['desc']
    if current_user.user.level < 10:
        if data['group']:
            user.group = model.Group.objects.get(id=data['group'])
    else:
        user.group = current_user.user.group

    user.save()


@trace(__name__)
def update(data):
    user = model.User.objects.get(name=data['name'])
    if user.pasd:
        user.pasd = common.hash(user.name + data['pasd'])
    user.level = int(data['level'])
    user.formalname = data['formalname']
    user.phones = []
    user.phones.append(data['phone'])
    user.address = data['address']
    user.gender = data['gender']
    user.email = data['email']
    user.desc = data['desc']
    if current_user.user.level < 10:
        if data['group']:
            user.group = model.Group.objects.get(id=data['group'])
    else:
        user.group = current_user.user.group

    user.save()
    return user.toDict()
