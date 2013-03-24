#!/usr/bin/python
#
# olaandcarly site settings
#

# system imports
import os
import socket

DEBUGGING_HOSTS = [ 'svart', 'silver' ]
HOSTNAME = socket.gethostname()
if HOSTNAME in DEBUGGING_HOSTS:
    from settings_debug import *
else:
    from settings_production import *

from settings_secret import *
