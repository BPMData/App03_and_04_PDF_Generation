from fpdf import FPDF
from funcs import get_minion
import pandas as pd

pdf = FPDF(orientation="landscape", unit="mm", format="A4")
get_minion(pdf)


df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="MinionBold", size=24)
    pdf.set_text_color(254, 0, 0)
    # the tuple passed to set_text_color is [Red, Green, Blue], min = 0, max = 254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(12,20, 200, 20)

# A problem with using Minion is you'll have to specify a different file type directly for italics, underlined, bold, etc...
# Actually, underlined is okay.

# Sad to say but I might just go with Courier or Times...
# BUT NOT RIGHT NOW!

# pdf.add_page()
# pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1, border=1)

pdf.output(("output.pdf"))