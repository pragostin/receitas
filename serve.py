#!/usr/bin/env python3
import os, sys
os.chdir('/Users/petersonagostinho/Documents/workspace/Receitas')
port = int(os.environ.get('PORT', 8091))
import http.server
handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(('', port), handler) as httpd:
    print(f'Serving at http://localhost:{port}', flush=True)
    httpd.serve_forever()
