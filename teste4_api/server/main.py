# Importando bibliotecas necessárias
from flask import Flask, request, jsonify

# Informações sobre o script
__author__ = "Rafael Malcervelli"
__contact__ = "r.malcervelli@gmail.com"
__version__ = "1.0.0"

# Função principal
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('data')
    print(request)
    print(data, flush=True)
    # Do something with the data, for example, sending it to a database or processing it
    return jsonify({'response': 'Data received'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)