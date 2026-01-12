from fpdf import FPDF 
import pandas as pd


pdf = FPDF(orientation='P', unit="mm", format="A4")

#padas is used for data analysis and investigation 
df = pd.read_csv('topics.csv')

# syntax within padas for going through each row of the data in the csv file
for index, row in df.iterrows():
    pdf.add_page() 
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt="hello there!", align="L", ln=1)
    # pdf.line(x1, y1, x2, y2)
    pdf.line(10, 22, 200, 22)

    for i in range(row['Pages'] - 1):
        pdf.add_page()

    

pdf.output("output.pdf")