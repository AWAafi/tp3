from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import de CORS

app = Flask(__name__)
CORS(app)  # ✅ Autorise les requêtes Cross-Origin (depuis file:// etc.)

@app.route('/api/square', methods=['GET'])
def square():
    try:
        number = int(request.args.get('number'))
        return jsonify({'result': number * number})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
