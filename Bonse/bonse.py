from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True)

for filepath in filepaths:
    filename = Path(filepath).stem.title()
    pdf.add_page()
    pdf.set_font(family="Courier", style="B", size=16)
    pdf.cell(w=0, h=16, txt=f"{filename}", ln=1, align="L")
    print(filename.lower())

    with open(f"{filename.lower()}.txt", "r") as file:
        content = file.read()
        pdf.set_font(family="Courier", size=10, style="B")
        pdf.multi_cell(w=0, h=10, txt=content)

pdf.output("output.pdf")

