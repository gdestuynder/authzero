#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2017 Mozilla Corporation
# Contributors: Guillaume Destuynder <kang@mozilla.com>


import logging
import time
import json
import sys
from authzero import AuthZero

class DotDict(dict):
    """return a dict.item notation for dict()'s"""

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = DotDict(value)
            self[key] = value

formatstr="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
logging.basicConfig(format=formatstr, datefmt="%H:%M:%S", stream=sys.stdout)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

config = DotDict(json.load(open("demo.json")))
authzero = AuthZero(config)
logger.debug("Auth0 initialized")
authzero.get_access_token()
logger.debug("Got access token")
#users = authzero.get_users(query_filter='identities.connection:"Mozilla-LDAP"')
#logger.debug("Got users:\n{}".format(users))
clients = authzero.get_clients()
logger.debug("Got clients:\n{}".format(clients))
