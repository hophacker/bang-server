from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor, protocol
from twisted.internet import reactor
from twisted.enterprise import adbapi
from twistar.registry import Registry
from twistar.dbobject import DBObject
from twisted.web import server, resource
from pprint import pprint
import os

Registry.DBPOOL= adbapi.ConnectionPool("MySQLdb", user="root", passwd="root", db = "bang");

class user(DBObject):
    pass


def done_user(user):
    print "added ";
    reactor.stop()


def check_user(_username):
    user.exists(['username = ?', _username]).addCallback(None)
    user.findBy(username=_username)
    #pprint(user.find(where=['username=?', _username], limit=1))

def register_user(_username, _contact, _email):
    u = user(username = _username, contact = _contact, email = _email)
    u.save().addCallback(done_user);
    #check_user(_username)

def finish():
    dbpool.close()
    reactor.stop()

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "{0}".format(request.args.keys())
        

    def render_POST(self, request):
        args = request.args
        type = args['type'][0]
        if type == "gps":
            print "gps"
            longitude = args['longitude'][0]
            latitude = args['latitude'][0]
            print longitude, latitude
        elif type == "register":
            register_user(args['username'][0], args['contact'][0], args['email'][0]);
            for arg in request.args.keys():
                print arg, args[arg][0]

        request.write("hoo");
        request.finish()
        return server.NOT_DONE_YET



class BangProtocol(protocol.Protocol):
    def dataReceived(self, data):
        print data
        #rows =  data.split(";")
        #print rows[0]
        self.transport.write("I'm Jie")
        self.transport.loseConnection()

class BangFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return BangProtocol()

site = server.Site(Simple())
reactor.listenTCP(80, site)
reactor.run()


#reactor.listenTCP(80, BangFactory())
#reactor.run()
