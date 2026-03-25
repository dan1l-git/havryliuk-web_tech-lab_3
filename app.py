import ssl
from flask import Flask

app = Flask(__name__)

STUDENT_NAME = "Havryliuk Danylo"
STUDENT_GROUP = "KP-33"

@app.route('/hello')
def hello():
    return f"Hello from {STUDENT_NAME} {STUDENT_GROUP}"


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('localhost.pem', 'localhost-key.pem')
    context.set_ciphers('AES128-SHA:AES256-SHA')

    app.run(host='localhost', port=5000, ssl_context=context)