cd ~/git/lua-lingrbot
git pull --rebase
cp -p ./index.cgi ~/public_html/cgi-bin/lua-lingrbot.cgi

cd ~/public_html/cgi-bin
if [ ! -e underscore.lua ]; then
  wget 'https://raw.github.com/mirven/underscore.lua/0.4-0/lib/underscore.lua'
fi
