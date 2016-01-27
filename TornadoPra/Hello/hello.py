# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))


class StoryHandler(tornado.web.RequestHandler):

    def get(self, story_id):
        self.write("you request the story" + story_id)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/[0-9]+/", StoryHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
