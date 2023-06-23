from fpdf import FPDF
from funcs import get_minion
import pandas as pd
import glob
from pathlib import Path
import os
import datetime as time

# pdf = FPDF(orientation="p", unit="mm", format="A4")
# get_minion(pdf)
# Weirdly, this has to be INSIDE the for loop, or pdf.image() does NOT work.
# Everything else works fine, though?

filepaths = glob.glob("invoice_data/*xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    get_minion(pdf)
    pathname = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family="MinionBold", size=16)
    pdf.cell(w=50, h=8, txt="Invoice #" + pathname[0:5], ln=1)
    date = pathname[6:]
    parsed_date = time.datetime.strptime(date, '%Y.%m.%d')
    formatted_date = parsed_date.strftime("%m/%d/%Y")
    pdf.cell(w=50, h=8, txt="Date was: " + formatted_date, ln=1)
    pdf.ln(10)
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Add header
    headers = list(df.columns)
    headers = [item.replace("_", " ").title() for item in headers]
    pdf.set_font(family="MinionImpact", size=10)
    pdf.set_fill_color(178, 255, 255) # Celeste. Thanks https://rgbcolorcode.com/color/B3FFFF
    pdf.set_text_color(255, 178, 178) # Melon, the complement of Celeste.
    # Too light. Darker?
    pdf.set_text_color(255, 80, 80) # "Tomato". Going up actually makes a color lighter.
    pdf.cell(w=30, h=8, txt=headers[0], border=1, fill=True, align="C")
    pdf.cell(w=70, h=8, txt=headers[1], border=1, fill=True, align="C")
    pdf.cell(w=30, h=8, txt=headers[2], border=1, fill=True, align="C")
    pdf.cell(w=30, h=8, txt=headers[3], border=1, fill=True, align="C")
    pdf.cell(w=30, h=8, txt=headers[4], border=1, ln=1, fill=True, align="C")
    # Add rows
    for index, row in df.iterrows():
        pdf.set_fill_color(222, 255, 255)
        pdf.set_font(family="Minion", size=12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1, align="C", fill=True)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1, align="C", fill=True)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1, align="C", fill=True)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1, align="C", fill=True)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1, align="C", fill=True)
        # To be supremely lazy, you can use win+shift+T to open the PowerToys text extractor, lol.

    # Adding the total total price
    pdf.cell(w=130, h=8, txt="", border=1, align="C", fill=True) # Its width is 30+70+30
    pdf.set_text_color(255, 60, 60)
    pdf.set_font(family="Minion", size=10)
    pdf.cell(w=30, h=8, txt=str("Total Invoice Cost:"), border=1, align="R", fill=True)
    pdf.cell(w=30, h=8, txt=str(df["total_price"].sum()), border=1, ln=1, align="C", fill=True)
    # could also use invoice_nr = filename.split("-")[0], which is technically more scalable.
    # My method will break if you have an invoice that is more or less than 5 digits long.
    # Or even bettter, invoice, date = filename.split("-")



    # Add text to bottom of invoice
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("MinionBold", size = 14)
    pdf.cell(w=0, txt=f"The total cost of your invoice is ${df['total_price'].sum()}.", ln=1)

    # Add company name and logo
    pdf.ln(10)
    pdf.set_text_color(255, 128, 0)
    pdf.set_font("MinionImpactItal", size=24)
    pdf.cell(w=70, h=12, txt=f"The Sunset Riders")
    pdf.image("company_logo.jpg", w=25)

    if not os.path.exists("invoice_pdfs_2"):
        os.mkdir("invoice_pdfs_2")
    pdf.output(f"invoice_pdfs_2/{pathname}.pdf")

