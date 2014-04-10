from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import csv

data_file = 'data.csv'
course_name = 'COS 212'


def create_report(data_file):
    pdf_name = course_name + ' Marksheet.pdf'
    c = canvas.Canvas(pdf_name, pagesize = A4)
    heighty = 700
    #header text
    c.drawCentredString(125, 800, course_name)
    testr1 = 'Student Number P1 ST1 T1 T2'
    c.drawCentredString(125, 700, testr1)
    marks_data = csv.reader(open(data_file, "rb"))
    for row in marks_data:
        st_num = row[0]
        p1 = row[1]
        st1 = row[2]
        t1 = row[3]
        t2 = row[4]
        
        heighty -= 100
        testr2 = row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4]
        c.drawCentredString(125, heighty, testr2)
        
    #save pdf page, use for each page
    c.showPage()
    #print 'created'
    c.save()
    
create_report(data_file) 
