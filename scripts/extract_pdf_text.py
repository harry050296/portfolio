import sys
from pdfminer.high_level import extract_text

if len(sys.argv) < 3:
    print('Usage: extract_pdf_text.py <input.pdf> <output.txt>')
    sys.exit(1)

input_pdf = sys.argv[1]
output_txt = sys.argv[2]

try:
    text = extract_text(input_pdf)
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Wrote extracted text to {output_txt}')
except Exception as e:
    print('Error extracting text:', e)
    sys.exit(2)
