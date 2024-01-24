from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob('Text+Files/*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:

    pdf.add_page()
    filename = Path(filepath).stem.capitalize()

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=0, h=8, txt=filename, align='L', ln=1)

    with open(filepath, 'r') as file:
        text_for_pdf = file.read()

    pdf.set_font(family='Times', size=16)
    pdf.multi_cell(w=0, h=8, align='L', txt=text_for_pdf)
pdf.output(f'PDFs/animals.pdf')
