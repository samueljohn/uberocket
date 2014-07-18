#!/usr/bin/env python3
# Based on the work of https://gist.github.com/FiloSottile/7634541

import http.server
import sys
import time
import urllib.parse
import json


HOST_NAME = sys.argv[1]
PORT_NUMBER = int(sys.argv[2])


def handle_hook(payload):
    pass
    # - todo -
    # git pull
    # git submodule update? or what?
    # pelican run (this can be done inside python from here)


class HookHandler(http.server.BaseHTTPRequestHandler):
    server_version = "HookHandler/0.2"

    def do_GET(s):
        s.send_response(200)
        s.wfile.write('Hello!')

    def do_POST(s):
        # Check that the IP is within the GH ranges
        if not any(s.client_address[0].startswith(IP)
                   for IP in ('192.30.252',
                              '192.30.253',
                              '192.30.254',
                              '192.30.255',
                              '127.0.0.1')):
            s.send_error(403)

        length = int(s.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(s.rfile.read(length).decode('utf-8'))
        payload = json.loads(post_data['payload'][0])

        handle_hook(payload)

        s.send_response(200)


if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HookHandler)
    print((time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print((time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)))
