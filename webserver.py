from pprint import pprint
from twisted.application.internet import TCPServer
from twisted.application.service import Application
from twisted.web.resource import Resource
from twisted.web.server import Site


class FormPage(Resource):
    def render_GET(self, request):
        return ''

    def render_POST(self, request):
        pprint(request.__dict__)
        newdata = request.content.getvalue()
        print newdata
        return ''


root = Resource()
root.putChild("form", FormPage())
application = Application("My Web Service")
TCPServer(8880, Site(root)).setServiceParent(application)
