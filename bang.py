from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.enterprise import adbapi
from twistar.registry import Registry
from twistar.dbobject import DBObject

class User(DBObject):
    pass

Registry.DBPOOL= adbapi.ConnectionPool("MySQLdb", 
        user="root",
        passwd="root",
        db = "bang");

def done(user):
    print "added"
    reactor.stop()

def register(name, phone):
    transaction.execute("insert into user (name, phone) values(?, ?)", (name, phone))

def finish():
    dbpool.close()
    reactor.stop()

class BangProtocol(LineReceiver):
    def __init__(self, factory):
        return



class BangFactory(Factory):
    def __init__(self):
        return
    def buildProtocol(self, addr):
        return BangProtocol(self)


users = [("jane", "jokerfeng2010@gmail.com"), ("joel", "ho@126.com")]

for _name, _phone in users:
    u = User(name = _name, phone = _phone)
    u.save().addCallback(done)
#reactor.listenTCP(80, BangFactory())
reactor.run()
