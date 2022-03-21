"""
Helper functions used throughout the project
"""
import datetime
import json
import random
import string
import uuid
import hashlib
import logging
from pathlib import Path
import tempfile
import os

class Utils:

    def __init__(self):
        self.date = str(datetime.datetime.now()).split(" ")[0]
        self.fname = "whalehoney-" + self.date + ".log"
        self.filepath = Path("logs/%s/%s" % (self.date, self.fname))
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.formatter = logging.Formatter("%(message)s")

    def setup_logger(self, name):
        """
        :param name: name of logger to setup
        :return:
        """

        handler = logging.FileHandler("./logs/%s/whalehoney-%s.log" % (self.date, self.date))
        handler.setFormatter(self.formatter)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        return logger

    def generate_random_data(self):
        """
        :return: string value of "random" data to be used in Docker API responses
        """
        return "".join(hashlib.sha256(uuid.uuid4()).hexdigest())

    def save_request_obj(self, request):
        req_data = {}
        req_data['date'] = str(datetime.datetime.now())
        req_data['endpoint'] = str(request.endpoint)
        req_data['method'] = str(request.method)
        req_data['cookies'] = str(request.cookies)
        req_data['data'] = str(request.data)
        req_data['headers'] = str(dict(request.headers))
        req_data['args'] = str(request.args)
        req_data['form'] = str(request.form)
        req_data['remote_addr'] = str(request.remote_addr)
        files = []
        for name, fs in request.files.items():
            dst = tempfile.NamedTemporaryFile()
            fs.save(dst)
            dst.flush()
            filesize = os.stat(dst.name).st_size
            dst.close()
            files.append({'name': name, 'filename': fs.filename, 'filesize': filesize,
                          'mimetype': fs.mimetype, 'mimetype_params': fs.mimetype_params})
        req_data['files'] = files

        return json.dumps(req_data)

    def gen_container_id(self):
        id = list(string.hexdigits)
        random.shuffle(id)
        return "".join(id[0:11]).lower()
