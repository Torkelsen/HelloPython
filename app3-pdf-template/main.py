import pandas as pd
from fpdf import FPDF

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(200,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10,y1=21,x2=200,y2=21)

    #make lines
    for y in range(33, 280, 12):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    #Set the footer
    pdf.ln(265) #breakline
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # make lines
        for y in range(24, 280, 12):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

        # Set the footer
        pdf.ln(277)  # breakline
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")