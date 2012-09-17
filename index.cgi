#!/usr/bin/lua
cjson = require 'cjson'
print "Content-Type: text/plain"
print ""
json = cjson.decode(io.read('*all'))
for _, x in ipairs(json.events) do
  _, _, body = string.find(x, '^!lua (.*)')
  io.write(body)
  -- io.write(x.message.nickname)
end
