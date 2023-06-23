from fpdf import FPDF
from funcs import get_minion
import pandas as pd
import glob
from pathlib import Path
import os

pdf = FPDF(orientation="p", unit="mm", format="A4")
get_minion(pdf)

filepaths = glob.glob("invoice_data/*xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    pathname = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family="MinionBold", size=16)
    pdf.cell(w=50, h=8, txt="Invoice #" + pathname[0:5], ln=1)
    pdf.cell(w=50, h=8, txt="Date " + pathname[6:])
    # could also use invoice_nr = filename.split("-")[0], which is technically more scalable.
    if not os.path.exists("invoice_pdfs"):
        os.mkdir("invoice_pdfs")
    pdf.output(f"invoice_pdfs/{pathname}.pdf")


testpath = Path(filepaths[0]).stem
print(testpath[0:5])




