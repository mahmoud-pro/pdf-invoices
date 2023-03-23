import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("./Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice_number, date = filename.split("-")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.add_page()

    pdf.set_font(family="Courier", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice No.{invoice_number}", ln=1)

    pdf.set_font(family="Courier", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    pdf.output(f"PDF/{filename}.pdf")
