#!/usr/bin/python3
"""
This script contains a Fabric function to create a
tar gzipped archive of the web_static directory.
"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a tar gzipped archive of the
    web_static directory.

    Returns:
        str: The path of the archive
        file if it was successfully created,
        or None if the creation failed.
    """
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive = "versions/web_static_{}.tgz".format(now)

    # Create the versions directory if it does not exist.
    local("mkdir -p versions") if not os.path.isdir("versions") else None

    # Create the tar gzipped archive of the web_static directory.
    result = local("tar -cvzf {} web_static".format(archive))

    return None if result.failed else archive
