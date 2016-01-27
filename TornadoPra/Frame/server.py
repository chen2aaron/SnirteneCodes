#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-6-9
# Blog: morningchen.com


import tornado.ioloop
import tornado.options
import tornado.httpserver

from applicatioin import application
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print "服务器正在运行在 http://127.0.0.1:%s" % options.port
    print "退出请按 Control-C"
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
