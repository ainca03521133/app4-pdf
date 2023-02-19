from fpdf import FPDF
import pandas as pd



pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto = False, margin=0)

df = pd.read_csv('app4-pdf/topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    #set header
    pdf.set_font(family="Times", style="B",size = 22)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0 ,h=12, txt=row["Topic"], align="L",ln=1)
    for y in range(20, 298, 10):
        pdf.line(10,y, 200,y)
    

    pdf.ln(260)#  A4 298mm
    pdf.set_font(family="Times", style="B",size = 8)
    pdf.set_text_color(200,200,200)
    pdf.cell(w=0,h=10, txt=row["Topic"], align="R")
   
    

    for i in range(row['Pages']-1):
        pdf.add_page()
        #set footer
        pdf.ln(277)#  A4 298mm
        pdf.set_font(family="Times", style="B",size = 8)
        pdf.set_text_color(200,200,200)
        pdf.cell(w=0,h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(10,y, 200,y)


pdf.output("output.pdf")