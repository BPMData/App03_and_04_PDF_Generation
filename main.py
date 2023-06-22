from fpdf import FPDF
from funcs import get_minion

pdf = FPDF(orientation="landscape", unit="mm", format="A4")

get_minion(pdf)

pdf.set_font(family="MinionImpactItal", style="U", size=12)

# A problem with using Minion is you'll have to specify a different file type directly for italics, underlined, bold, etc...
# Actually, underlined is okay.

# Sad to say but I might just go with Courier or Times...
# BUT NOT RIGHT NOW!

pdf.add_page()

pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1, border=1)

pdf.output(("outputMinionBOLDU3.pdf"))