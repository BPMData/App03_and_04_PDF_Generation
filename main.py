from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

print(pdf)

pdf.add_font(family="Minion", fname="C:\Fonts\Minion\TTF\MinionProReg.ttf",
            uni=True)

pdf.add_font(family="MinionItal", fname="C:\Fonts\Minion\TTF\MinionProItal.ttf",
            uni=True)

pdf.add_font(family="MinionBold", fname="C:\Fonts\Minion\TTF\MinionProBold.ttf",
            uni=True)

pdf.add_font(family="MinionBoldItal", fname="C:\Fonts\Minion\TTF\MinionProBoldItal.ttf",
            uni=True)

pdf.add_font(family="MinionImpact", fname="C:\Fonts\Minion\TTF\MinionProBigBold.ttf",
            uni=True)

pdf.add_font(family="MinionImpactItal", fname="C:\Fonts\Minion\TTF\MinionProBigBoldItal.ttf",
            uni=True)

pdf.set_font(family="MinionImpactItal", style="U", size=12)

# A problem with using Minion is you'll have to specify a different file type directly for italics, underlined, bold, etc...
# Actually, underlined is okay.


# Sad to say but I might just go with Courier or Times...
# BUT NOT RIGHT NOW!

pdf.add_page()

pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1, border=1)

# pdf.output(("outputMinionBOLDU.pdf"))