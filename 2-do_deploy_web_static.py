#!/usr/bin/python3
""" fabric script to distribute an archive to 
web servers using do_deploy
"""

import os

from fabric.api import *
from os.path import exists, basename

env.hosts = ['3.95.60.27', '52.90.161.53']
env.user = 'ubuntu'


def do_deploy():
    """
    Distributes an archive to the web servers
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_name = basename(archive_path)
        archive_name_noext = archive_name.split(".")[0]
        run('sudo mkdir -p /data/web_static/releases/{}/'.format(
            archive_name_noext))
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(archive_name, archive_name_noext))
        run('sudo rm /tmp/{}'.format(archive_name))
        run('sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
            archive_name_noext, archive_name_noext))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'.
            format(archive_name_noext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(archive_name_noext))
        print("New version deployed!")
        return True
    except:
        return False
