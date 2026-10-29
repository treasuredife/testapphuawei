import os, socket, time
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8080"))
DEPLOYED_TAG = os.environ.get("APP_VERSION", "unknown")   # set by docker run -e
BUILD_COMMIT = os.environ.get("GIT_SHA", "unknown")       # baked in at build time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body, ctype = b"OK", "text/plain"
        else:
            html = f"""<html><body style="font-family:sans-serif;margin:0">
<div style="background:#1a7f37;color:#fff;padding:24px 40px">
  <h1 style="margin:0">Docker on ECS test: VERSION 2 (green)</h1>
</div>
<div style="padding:24px 40px">
  <p><b>Deployed tag (docker run):</b> {DEPLOYED_TAG}</p>
  <p><b>Build commit (baked into image):</b> {BUILD_COMMIT}</p>
  <p><b>Container ID (hostname):</b> {socket.gethostname()}</p>
  <p><b>Server time:</b> {time.strftime('%Y-%m-%d %H:%M:%S %Z')}</p>
</div></body></html>"""
            body, ctype = html.encode(), "text/html"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
