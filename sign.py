#
# Requirements: pdftk, pdftotext, python
#
#  Arturo Montejo - 2020
#

# Parameters
INPUT_PDF = 'PDFborrador.pdf'
SIGNATURE = 'signature.pdf'
CODES = 'codigos.csv'

import os
import re
import subprocess

# Extract pages
print("Extracting pages")
os.system(f'pdftk {INPUT_PDF} burst')

# Generate list of pages
pages = []
for filename in os.listdir('./'):
    if re.match(r'pg_[0-9]+.pdf', filename):
        pages.append(filename)
pages.sort()

# Create dictionary of DNI -> codes
print("Reading codes")
dni2code = {}
with open(CODES) as fh:
    for l in fh:
        dni, code = re.split(r'[^0-9A-Z]', l.strip())[-2:]
        dni2code[dni] = code

# Loop over pages 
print("Signing")
for i, p in enumerate(pages):
    
    # Extract employee's DNI
    if i % 2 != 0: # par        
        out = subprocess.Popen(['pdftotext', p, '-'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, _ = out.communicate()
        content = str(stdout[:1000])
        dni = re.search(r'[A-Z]*[0-9]+[A-Z]+', content)

        if dni and dni[0] in dni2code:
            dni = dni[0]
        else: 
            continue

        print(f"** processing employee {dni}")
        # Sign
        p_signed = p.split('.')[0] + '_signed.pdf'
        os.system(f'pdftk {p} stamp {SIGNATURE} output {p_signed}')

        # Compose final document 
        os.system(f'pdftk {p_prev} {p_signed} cat output output/{dni2code[dni]}.pdf')
    else:
        p_prev = p
    

# Clean up everything
print("Cleaning up")
os.system('rm pg_*.pdf')

print("Done!")