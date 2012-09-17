#!/usr/bin/lua
cjson = require 'cjson'
print "Content-Type: text/plain"
print ""
json = cjson.decode(io.read('*all'))
io.write(json.events[1].message.nickname)
