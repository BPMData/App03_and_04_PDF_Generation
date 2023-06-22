from fpdf import FPDF
# import pathlib
# minionpath = pathlib.PureWindowsPath("C:\Users\corma\AppData\Local\Microsoft\Windows\Fonts\MinionPro-Regular.otf")
# print(minionpath)

pdf = FPDF(orientation="portrait", unit="mm", format="A4")


print(type(pdf))

print(dir(pdf))



pdf.add_font(family="MinionReg", fname="C:\Fonts\Minion\MinionPro-Regular.ttf",
            uni=True)
pdf.set_font(family="MinionReg", size=12)

pdf.add_page()

pdf.cell(w=0,h=12,txt="Hello There", align="L", ln=1, border=1)

pdf.output(("output.pdf"))