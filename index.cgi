#!/usr/bin/lua
cjson = require 'cjson'
_ = require 'underscore'
json = cjson.decode(io.read('*all'))
local result = _(json.events):chain():map(function(x)
  return {select(3, string.find(x.message.text, '^!lua (.*)')), x.message}
end):filter(function(xs)
  local body, message = xs[1], xs[2]
  return body and message.room == 'computer_science'
end):map(function(xs)
  body, message = xs[1], xs[2]
  io = {write = io.write}
  os = {date = os.date, time = os.time}
  return assert(loadstring(string.format('return tostring(%s)', body)))()
end):join("\n"):value()

print "Content-Type: text/plain"
print string.format("Content-Length: %d", #result)
print ""
io.write(result)
