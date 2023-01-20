# Importando bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import os, zipfile

# Informações sobre o script
__author__ = "Rafael Malcervelli"
__contact__ = "r.malcervelli@gmail.com"
__version__ = "1.0.0"

# Função para baixar arquivos
def download_file(url, file_path):
    response = requests.get(url)
    open(file_path, 'wb').write(response.content)

# Função principal
def main():
    try:
        url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        pdf_links = []
        xlsx_links = []

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                if href.endswith('.pdf'):
                    pdf_links.append(href)
                elif href.endswith('.xlsx'):
                    xlsx_links.append(href)

        pdf_folder = 'pdf_files/'
        xlsx_folder = 'xlsx_files/'

        if not os.path.exists(pdf_folder):
            os.makedirs(pdf_folder)
        if not os.path.exists(xlsx_folder):
            os.makedirs(xlsx_folder)

        for link in pdf_links:
            file_name = link.split('/')[-1]
            if "Anexo" in file_name:
                file_path = pdf_folder + file_name
                download_file(link, file_path)
            
        for link in xlsx_links:
            file_name = link.split('/')[-1]
            if "Anexo" in file_name:
                file_path = xlsx_folder + file_name
                download_file(link, file_path)
            
        print("[+] All files downloaded!")

        with zipfile.ZipFile('all_downloaded_files.zip', 'w') as zip_file:
            for root, dirs, files in os.walk(pdf_folder):
                for file in files:
                    zip_file.write(os.path.join(root, file))
            for root, dirs, files in os.walk(xlsx_folder):
                for file in files:
                    zip_file.write(os.path.join(root, file))
        
        print("[+] Files zipped!")
    except:
        print("[x] Error!")


# Executa a função main
if __name__ == '__main__':
    main()