import re
import pdfplumber

def extrated_name_file(file,sufix=''):
    padrao = re.compile(r"^C\d+\s*-\s*[A-Za-zÀ-ÿ\s]+$")

    with pdfplumber.open(file.file) as pdf:
        lines = pdf.pages[0].extract_text().split("\n")

        ine = lines[1].split("=")[1]

        for line in lines:
            if padrao.match(line):
                indicative_line = line.split("Unidade")
                name_indicative = indicative_line[0].replace(' ','_').replace('-','')

                break
    file.file.seek(0)

    return f"{name_indicative}{sufix}.pdf"