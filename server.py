import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.template

WWW_ROOT = "/var/pywww/"
WWW_PORT = 8080

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", Index),
			(r"/submit", Submit),
		]
		tornado.web.Application.__init__(self, handlers)

class Index(tornado.web.RequestHandler):
	def get(self):
		self.render(WWW_ROOT + "index.html")

class Submit(tornado.web.RequestHandler):
	def post(self):
		name = ''.join(self.request.arguments['name'])
		loader = tornado.template.Loader(WWW_ROOT)
		self.finish(loader.load("submit.html").generate(tpl_name = name))

def main():
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(WWW_PORT)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
