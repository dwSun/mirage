#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base import *


class SConfig(DbFun, db.Document):
    pitems = db.IntField(default=20)
