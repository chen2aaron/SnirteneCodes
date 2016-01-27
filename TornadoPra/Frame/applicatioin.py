from url import url

import tornado.web
import os

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True,
    )
application = tornado.web.Application(
    handlers=url,
    **settings
    )
