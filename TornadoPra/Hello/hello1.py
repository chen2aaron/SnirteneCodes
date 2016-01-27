import os.path
import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


# class ReverseHandler(tornado.web.RequestHandler):

#     def get(self, input):
#         self.write(input[::-1])


# class WrapHandler(tornado.web.RequestHandler):

#     def get(self):
#         widget = retrieve_from_db(widget_id)
#         self.write(widget.serialize())

#     def post(self):
#         text = self.get_argument('text')
#         width = self.get_argument('width', 40)
#         self.write(textwrap.fill(text, int(width)))


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


class PoemPageHandler(tornado.web.RequestHandler):

    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render(
            'poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)


class BookHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('book.html',
                    title="home page",
                    header="Book that great",
                    books=[
                        "Learning Python",
                        "Hhahahah",
                        "xixixiixixi",
                    ])
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/poem", PoemPageHandler),
            (r"/book", BookHandler),
            # (r"/reverse/(\w+)", ReverseHandler),
            # (r"/wrap", WrapHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
