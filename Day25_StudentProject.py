from fpdf import FPDF
from funcs import get_minion
import glob
from pathlib import Path
import os
import re

pdf = FPDF(orientation="p", unit="mm", format="A4")
get_minion(pdf)

filepaths = glob.glob("invoice_data/txts/*txt")

for filepath in filepaths:
    with open(filepath, "r") as file:
        lines = file.readlines()
        text = "".join(lines)

        """# The more elegant solution, going forward, is just use file.read(), which
        # will read the entire .txt file as a single string with line breaks interpreted rather than
        # printed literally!
        
        But x = file.readlines()
        y = ''.join(x) 
        
        However, obviously not as elegant as:
        
        x = file.read()
        
        also works.
        """

        text = re.sub(r'\[\d+\]', "", text)
        text = text.replace('\n', '\n    ')
    pathname = Path(filepath).stem
    pdf.add_page()
    # Generate page header/title
    pdf.set_font(family="MinionImpactItal", size=36)
    pdf.cell(w=0, h=18, txt=f"{pathname.title()}", ln=2, align="C",
             fill=False, border=True)
    # Generate body text
    pdf.set_font(family="Minion", size=14)
    pdf.multi_cell(w=0, h=12, txt=f"    {text}", border=0)

if not os.path.exists("invoice_data/txts/pdfs"):
    os.mkdir("invoice_data/txts/pdfs")
pdf.output(f"invoice_data/txts/pdfs/concat4_indents.pdf")
