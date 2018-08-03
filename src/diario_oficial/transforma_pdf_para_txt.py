import re
import PyPDF2


pdf_file_object = open('/home/wfirmino/.virtualenvs/env_webserrana/src/media/uploads/concursos/ps_2016_03/edital_abertura_ps-03-2016_pmserrana(1).pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
num_pages = pdf_reader.numPages

texto_lista = []

for i in range(0, num_pages):
    page_object = pdf_reader.getPage(i)
    texto_lista.append(page_object.extractText())

texto_string = " ".join(texto_lista).lower()

entry_text = str(input("Pesquisar texto ->"))

try:
    pesquisa = re.search(entry_text, texto_string)
    print(pesquisa.group(0))
