#!/usr/bin/env python3
# Based on the work of https://gist.github.com/FiloSottile/7634541

import sys
sys.path.insert(0, '')  # to import local flipflop module
import flipflop
from cgi import escape
import json


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    yield '<h1>FastCGI Environment</h1>'
    yield '<table>'
    for k, v in sorted(environ.items()):
        yield '<tr><th>%s</th><td>%s</td></tr>' % (escape(k), escape(v))
    yield '</table>'


if __name__ == '__main__':
    print("Starting fcgi server ...")
    flipflop.WSGIServer(app).run()

    # - todo -
    # git pull
    # git submodule update? or sync or what?
    # pelican run (this can be done inside python from here)


    # Check that the IP is within the GH ranges
    # if not any(s.client_address[0].startswith(IP)
    #            for IP in ('192.30.252',
    #                       '192.30.253',
    #                       '192.30.254',
    #                       '192.30.255',
    #                       '127.0.0.1')):
