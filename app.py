from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/convert')
def convert():
    celsius = request.args.get('celsius', type=float)
    fahrenheit = (celsius * 9/5) + 32
    return jsonify({"celsius": celsius, "fahrenheit": fahrenheit})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
