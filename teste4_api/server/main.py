# Importando bibliotecas necessárias
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from typing import Dict
import os

# Informações sobre o script
__author__ = "Rafael Malcervelli"
__contact__ = "r.malcervelli@gmail.com"
__version__ = "1.0.0"

# Define o diretório de trabalho
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Função principal
app = Flask(__name__)
CORS(app)
df = pd.read_csv('./../../teste3_databases/files/relatorio_teste3.csv', delimiter = ';', encoding = 'latin-1')

def search_dataframe(df: pd.DataFrame, data: Dict) -> pd.DataFrame:
    search_value = data.get('search_value')
    search_column = data.get('search_column')

    result = df[df[search_column].str.contains(search_value, na=False, case=False)]
    return result

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('data')
    result = search_dataframe(df, data)

    return jsonify({'response': 'Data received-> {}'.format(result.to_dict())})

if __name__ == '__main__':
    app.run(debug=True, port=5000)