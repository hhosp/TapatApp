from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Falten paràmetres'}), 400
    
    resultat = num1+num2
    return jsonify({'resultat' : resultat})

if __name__ == '__main__':
    app.run(debug=True)