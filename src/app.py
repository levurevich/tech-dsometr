from flask import Flask
import logging

app = Flask(__name__)

@app.route('/')
def main():
    return 'Current build number is: <build_number>\n'

if __name__ == '__main__':
    logging.basicConfig(filename='./logs/debug.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')