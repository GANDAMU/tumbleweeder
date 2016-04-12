#!/usr/bin/env python

import bottle

app = application = bottle.Bottle()

@app.route('/tumbleweed', method=['GET'])
def tumbleweeds():
    bottle.response.headers['Content-Type'] = 'text/plain'
    return {"response_type": "in_channel", "text":
        ":_tumbleweed_1: :_tumbleweed_2: :_tumbleweed_3: "
        ":_tumbleweed_4: :_tumbleweed_5: :_tumbleweed_6:" }

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
