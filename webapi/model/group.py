#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from .base import *


class Group(DbFun, db.Document):
    meta = {
        'indexes': [
            {
                'fields': ['name'],
                'unique': True
            }
        ]
    }
    name = db.StringField(required=True)
    contact = db.ReferenceField('User')
    desc = db.StringField()
