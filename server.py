from http.server import HTTPServer, BaseHTTPRequestHandler
import platform
import socket


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        hostname = socket.gethostname()
        processor = platform.processor()
        system = platform.system()
        version = platform.version()
        machine = platform.machine()

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Laptop Device Specifications</title>
        </head>

        <body>
            <h1>Simple Webserver</h1>

            <h2>Student Details</h2>
            <p>Name: Hemavarshini V</p>
            <p>Register Number: 26004751</p>

            <h2>Device Specifications</h2>
            <p>Device Name: {hostname}</p>
            <p>Processor: {processor}</p>
            <p>Operating System: {system}</p>
            <p>OS Version: {version}</p>
            <p>Machine Type: {machine}</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


server = HTTPServer(("127.0.0.1", 8000), MyServer)

print("Server running at http://127.0.0.1:8000")

server.serve_forever()
