#!/usr/bin/python3
""" fabric script to generate a .tgz archive
from the contents of the web_static folder of my AirBnB clone repo
"""

import os

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except:
        return None
