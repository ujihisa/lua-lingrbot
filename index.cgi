#!/usr/bin/lua
cjson = require 'cjson'
_ = require 'underscore'
print "Content-Type: text/plain"
print ""
json = cjson.decode(io.read('*all'))
_(json.events):each(function(x)
  body = string.find(x.message.text, '^!lua (.*)')[3]
  if body and x.message.room == 'computer_science' then
    io = {write = io.write}
    os = {date = os.date}
    loadstring(string.format('io.write(%s)', body))()
  end
end)
