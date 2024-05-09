from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello Flask'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # host='0.0.0.0' 설정시 아래 두 ip 모두 접속 가능
    # http://127.0.0.1:5000
    # http://192.168.35.47:5000
