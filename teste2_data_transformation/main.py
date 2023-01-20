# Importando bibliotecas necessárias
import os, zipfile, pdfplumber
import pandas as pd

# Informações sobre o script
__author__ = "Rafael Malcervelli"
__contact__ = "r.malcervelli@gmail.com"
__version__ = "1.0.0"

# Função para substituir valores
def replace_value(value):
    if value == "OD":
        return "Seg. Odontológica"
    elif value == "AMB":
        return "Seg. Ambulatorial"
    else:
        return value

# Função principal
def main():
    try:
        # Define o diretório de trabalho
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Define o diretório dos arquivos pdf
        with pdfplumber.open("../teste1_webscraping/pdf_files/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf") as pdf:
            tables_df = []

            for page in pdf.pages:
                table = page.extract_table()

                if table is not None:
                    table_df = pd.DataFrame(table[1:], columns=table[0])
                    tables_df.append(table_df)

            final_df = pd.concat(tables_df)
            print("[+] Table extracted!")

            final_df = final_df.applymap(replace_value)
            final_df.to_csv("output_files/anexo1.csv", index=False)
            print("[+] CSV created!")

        with zipfile.ZipFile('teste_rafael_malcervelli.zip', 'w') as zip_file:
            for root, dirs, files in os.walk("./output_files"):
                for file in files:
                    zip_file.write(os.path.join(root, file))
        
        print("[+] Files zipped!")
    except Exception as e:
        print("[x] Error!")
        print(e)

# Executa a função main
if __name__ == '__main__':
    main()