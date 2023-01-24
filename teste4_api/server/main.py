# Importando bibliotecas necessárias
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from typing import Dict
import os, json

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

def search_dataframe(df: pd.DataFrame, search_value: str, search_column: str) -> pd.DataFrame:
    try:
        result = df[df[search_column].str.contains(search_value, na=False, case=False)]
        return result
    except Exception as e:
        print(search_column)
        print(df.columns)
@app.route('/submit', methods=['POST'])
def submit():
    data = json.loads(request.data)
    search_value = data['search_value']
    search_column = data['search_column']
    result = search_dataframe(df, search_value, search_column)

    return jsonify(result.to_json(orient='index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)