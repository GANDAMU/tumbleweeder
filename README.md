# tumbleweeder #

Haphazard repo of my tumbleweed slack slash command

## Stole Some Shit ##

Source: http://www.deviantart.com/art/Tumbleweed-New-Asset-445527292
Source's source: http://kitkatyj.deviantart.com/art/Tumbleweed-Commission-445479266

## The GIFs ##

Should be pretty intuitive: if you put the GIFs next to each other, they combine to form one long "GIF." The crux of this thing is cutting up a long GIF into emoji-sized GIFs.

## The "Server" ##

If slack would let me make macros, that'd be enough for this to work. But since it doesn't, we need a braindead "server."

Honestly, you don't even need a "server." Just a link to a file with the following contents is probably enough:

    {"text": ":_tumbleweed_1: :_tumbleweed_2: :_tumbleweed_3: :_tumbleweed_4: :_tumbleweed_5: :_tumbleweed_6:", "response_type": "in_channel"}

I'm sure if you can set up a slack slash command, then you have your own preference for webservers. I wrote tumbleweeder.py in python out of habit. I have my personal server set up with nginx/uwsgi, also out of habit. So what's included isn't ACTUALLY how I run it. 

Or if you're laxy just point your slack slash command to: http://stacksarelast.info/tumbleweed
