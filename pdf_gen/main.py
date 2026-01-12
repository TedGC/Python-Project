from fpdf import FPDF 
import pandas as pd


pdf = FPDF(orientation='P', unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

#padas is used for data analysis and investigation 
df = pd.read_csv('topics.csv')

# syntax within padas for going through each row of the data in the csv file
for index, row in df.iterrows():
    pdf.add_page() 
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    # pdf.line(x1, y1, x2, y2)
    pdf.line(10, 22, 200, 22)

    # setting the footer for the master page
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # setting the footer for other pages 
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
            

pdf.output("output.pdf")