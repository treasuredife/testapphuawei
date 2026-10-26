import os, socket, time
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8080"))
VERSION = os.environ.get("APP_VERSION", "v1")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body, ctype = b"OK", "text/plain"
        else:
            html = f"""<html><body style="font-family:sans-serif;margin:40px">
<h1>Docker on ECS test: {VERSION}</h1>
<p><b>Container ID (hostname):</b> {socket.gethostname()}</p>
<p><b>Server time:</b> {time.strftime('%Y-%m-%d %H:%M:%S %Z')}</p>
</body></html>"""
            body, ctype = html.encode(), "text/html"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
