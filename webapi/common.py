#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import base64


def hash(text):
    sha = hashlib.sha256()
    sha.update(text.encode('ascii'))
    return base64.b64encode(sha.digest()).decode('ascii')


if __name__ == '__main__':
    print(hash('admin'+'secret'))
