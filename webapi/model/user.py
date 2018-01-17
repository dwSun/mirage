#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_mongoengine import MongoEngine, DoesNotExist, ValidationError
from mongoengine.errors import NotUniqueError
from datetime import datetime

from .base import *

GENDER = (('Male', '男'),
        ('Female', '女'))


class User(DbFun, db.Document):
    meta = {
        'indexes': [
            {
                'fields': ['name'],
                'unique': True
            }
        ]
    }
    name = db.StringField(required=True)
    pasd = db.StringField(required=True)
    level = db.IntField(required=True)

    formalname = db.StringField()
    avator = db.StringField()
    phones = db.ListField(db.StringField())
    address = db.StringField()
    gender = db.StringField(choices=GENDER)
    email = db.EmailField()
    group = db.ReferenceField('Group')

    desc = db.StringField()

    date = db.DateTimeField(default=datetime.now(tz))
