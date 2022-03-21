#!/usr/bin/env python3
try:
    import sys
    from dockerapi.docker_routes import *
except ImportError as ierr:
    print("[!] Import error %s" % ierr)
    sys.exit(1)

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=False, port=2375)
