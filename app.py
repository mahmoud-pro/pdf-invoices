import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("./Invoices/*.xlsx")

for filepath in filepaths:


    filename = Path(filepath).stem
    invoice_number, date = filename.split("-")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.add_page()

    pdf.set_font(family="Courier", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice No.{invoice_number}", ln=1)

    pdf.set_font(family="Courier", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns = df.columns
    columns = [item.replace("_", " ") for item in columns]

    pdf.set_font(family="Courier", size=10, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=55, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1)
    pdf.cell(w=35, h=8, txt=columns[3], border=1)
    pdf.cell(w=25, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Courier", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=55, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=25, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDF/{filename}.pdf")


