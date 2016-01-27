from . import BaseAPI
import json
import logging
import urllib.parse
from tornado.options import options
from eve.utils import json_hook


class Tongdun(BaseAPI):
    def __init__(self):
        super(Tongdun, self).__init__()

    def url(self):
        return options.tongdun_test

    def method(self):
        return 'POST'

    def before_request(self):
        self._fields.update({
            'event_id': 'loan_web',
            'partner_code': options.partner_code,
            'secret_key': options.secret_key,
            })

    def parse_response(self, response):
        response = response.decode('utf-8')
        response = urllib.parse.unquote(response)
        logging.info('tongdun response: %s', response)
        return json.loads(response, object_hook=json_hook)

    def is_ok(self, response):
        ok = response.success = 'true'
        if not ok:
            logging.error('tongdun request error')
        return ok