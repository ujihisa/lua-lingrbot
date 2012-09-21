#!/usr/bin/lua
cjson = require 'cjson'
print "Content-Type: text/plain"
print ""
json = cjson.decode(io.read('*all'))
for _, x in ipairs(json.events) do
  _, _, body = string.find(x.message.text, '^!lua (.*)')
  if body and x.message.room == 'computer_science' then
    io = {write = io.write}
    os = {date = os.date}
    loadstring(string.format('io.write(%s)', body))()
  end
end
