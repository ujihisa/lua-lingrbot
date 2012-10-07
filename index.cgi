#!/usr/bin/lua
cjson = require 'cjson'
_ = require 'underscore'
print "Content-Type: text/plain"
print "Content-Length: 1024"
print ""
json = cjson.decode(io.read('*all'))
_(json.events):each(function(x)
  body = select(3, string.find(x.message.text, '^!lua (.*)'))
  message = x.message
  if body and x.message.room == 'computer_science' then
    io = {write = io.write}
    os = {date = os.date, time = os.time}
    assert(loadstring(string.format('io.write(tostring(%s))', body)))()
  end
end)
