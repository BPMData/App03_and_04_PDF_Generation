from fpdf import FPDF
from funcs import get_minion
import pandas as pd
import glob
from pathlib import Path
import os

pdf = FPDF(orientation="p", unit="mm", format="A4")
get_minion(pdf)

pdf.add_page()
pdf.set_font(family="MinionBold", size=16)
pdf.cell(w=50, h=8, txt="Testing Adding an Image", ln=1)
pdf.image("pythonhow.jpeg", w=10)
pdf.image("company_logo.jpg", w=25)


pdf.output("imagetest.pdf")
