"""Imagine you're differentiating your student notebook for the type of kid who prefers lined paper.

You know: morons."""

from fpdf import FPDF
from funcs import get_minion
import pandas as pd

pdf = FPDF(orientation="landscape", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
# A4 in MM is 210 mm wide, 298 mm tall
get_minion(pdf)

df = pd.read_csv("topics.csv")

""" If you want only the first page to have a header and each subsequent page to be blank"""
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="MinionBold", size=24)
    pdf.set_text_color(254, 0, 0)
    # the tuple passed to set_text_color is [Red, Green, Blue], min = 0, max = 254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(12, 20, 200, 20)

    # We want a new line every 8 mm from 28 to 186

    for i in range(28, 196, 8):
        pdf.line(12, i, 270, i)

    pdf.ln(169)
    # pdf.line(12, 194, 290, 194)
    pdf.set_font(family="MinionItal", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=0)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for y in range(28, 196, 8):
            pdf.line(12, y, 270, y)

        pdf.ln(181)
        # pdf.line(12, 194, 290, 194)
        pdf.set_font(family="MinionItal", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=0)

"""If you want each page to have the topic header
for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="MinionBold", size=24)
        pdf.set_text_color(254, 0, 0)
        # the tuple passed to set_text_color is [Red, Green, Blue], min = 0, max = 254
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(12,20, 200, 20)
"""

pdf.output("output_lined.pdf")

# A problem with using Minion is you'll have to specify a different file type directly for italics,
# underlined, bold, etc...
# Actually, underlined is okay.

# Sad to say, but I might just go with Courier or Times...
# BUT NOT RIGHT NOW!

# pdf.add_page()
# pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1, border=1)

print("Print done")
