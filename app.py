# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello!"

@app.route('/ping')
def ping():
    return "Pong!"
    
if __name__ == '__main__':
    # Run the app on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
