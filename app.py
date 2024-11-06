from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_temperature():
    try:
        data = request.get_json()
        celsius = float(data['celsius'])
        fahrenheit = (celsius * 9/5) + 32
        return jsonify({'fahrenheit': fahrenheit})
    except Exception as e:
        return jsonify({'error': 'Error converting temperature. Please try again.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
