from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Current build number is: <build_number>\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0')