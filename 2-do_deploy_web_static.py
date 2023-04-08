#!/usr/bin/python3
"""
This script contains a Fabric function to deploy a
compressed archive of the web_static directory to a web server.
"""

from fabric.api import run, put, env
import os

env.hosts = ['3.86.13.33', '54.165.34.13']


def do_deploy(archive_path):
    """
    Distribute an archive to the web servers and deploy it.

    Args:
        archive_path (str): The local path of
        the archive file to deploy.

    Returns:
        bool: True if the deployment was successful,
        False otherwise.
    """
    # Check if the archive file exists.
    if not os.path.isfile(archive_path):
        return False
    else:
        file = archive_path.split("/")[-1]
        file_name = file.split(".")[0]
        if put(archive_path, "/tmp/").failed:
            return False
        if run(f"rm -rf /data/web_static/releases/{file_name}/").failed:
            return False
        if run(f"mkdir -p /data/web_static/releases/{file_name}").failed:
            return False
        if run(f"tar -xzf /tmp/{file} -C /data/web_static/"
               f"releases/{file_name}/").failed:
            return False
        if run(f"rm /tmp/{file}").failed:
            return False
        if run(f"mv /data/web_static/releases/{file_name}/web_static/* "
               f"/data/web_static/releases/{file_name}/").failed:
            return False
        if run(f"rm -rf /data/web_static/releases/"
               f"{file_name}/web_static").failed:
            return False
        if run("rm -rf /data/web_static/current").failed:
            return False
        if run(f"ln -s /data/web_static/releases/{file_name}/ "
               f"/data/web_static/current").failed:
            return False
        return True
