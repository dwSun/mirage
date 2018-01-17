#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_mongoengine import MongoEngine
import pytz
import json

db = MongoEngine()

tz = pytz.timezone('Asia/Shanghai')


class DbFun():
    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return self.to_json()

    def toDict(self):
        return json.loads(self.to_json())
