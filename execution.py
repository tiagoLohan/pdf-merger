import PyPDF2
import os
from tkinter.filedialog import askdirectory
import time

# Cria uma instância do objeto PdfMerger para juntar os PDFs
merger = PyPDF2.PdfMerger()

# Abre um pop-up para definir o caminho da pasta onde os PDFs estão localizados e onde será salvo o arquivo final.
path = askdirectory(title="Selecione a Pasta")

# Extrai o nome da pasta para usá-lo no nome do arquivo final
folder_name = os.path.basename(path)

# Cria o caminho completo para o arquivo final, usando o nome da pasta como parte do nome do arquivo
output_file = os.path.join(path, f"Pedido - {folder_name}.pdf")

# Lista todos os arquivos na pasta e ordena-os
files_list = os.listdir(path)
files_list.sort()

# Itera sobre os arquivos da pasta e adiciona os PDFs à junção
for file in files_list:
  if ".pdf" in file:  # Verifica se o arquivo é um PDF
    merger.append(f"{path}/{file}")  # Adiciona o PDF ao objeto merger

# Salva o arquivo PDF final no caminho especificado
merger.write(output_file)

# Exibe uma mensagem de sucesso no console com o nome do arquivo final
print(f"PDF merger sucess! ✅ name: Pedido completo - {folder_name}.pdf")
print("O terminal será fechado em 5 segundos...⏰´")

time.sleep(5)


