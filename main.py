import json


data = [ { 'Hola':'Hello', 'Hoi':"Hello", 'noun':"hello" } ]
print 'DATA:', (data)

json_encoded = json.dumps(data)
print json_encoded


decoded_data = json.loads(json_encoded)
print decoded_data
