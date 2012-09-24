#!/usr/bin/lua
cjson = require 'cjson'
_ = require 'underscore'
print "Content-Type: text/plain"
print ""
json = cjson.decode(io.read('*all'))
_(json.events):each(function(x)
  local body = select(3, string.find(x.message.text, '^!lua (.*)'))
  local message = x.message
  if body and x.message.room == 'computer_science' then
    io = {write = io.write}
    os = {date = os.date}
    assert(loadstring(string.format('io.write(tostring(%s))', body)))()
  end
end)
