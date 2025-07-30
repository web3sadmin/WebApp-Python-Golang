from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Unknown')
    
    return f"""
    <html>
        <body>
            <h1>Host Information</h1>
            <p><b>Hostname:</b> {hostname}</p>
            <p><b>IP Address:</b> {host_ip}</p>
            <p><b>Author:</b> {author}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
