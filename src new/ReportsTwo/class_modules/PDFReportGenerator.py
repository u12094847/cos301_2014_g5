from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator
from class_modules.ReportGenerator import Report
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import A4

import csv

class PDFReportGenerator(ReportGenerator):
  def __init__(self, _request):		#Constructor
    self.reportRequest = _request
  
  def __init__(self,report):		#Constructor
    self.report = report
    create_report(report)
  


#data_file = 'data20.csv'
course_name = 'COS 212'


def create_report(report):
    pdf_name = course_name + ' Marksheet.pdf'
    
    fnt = 'Helvetica'
    sz = 12
    
    c = canvas.Canvas(pdf_name, pagesize = landscape(A4)) 
    c.setFont(fnt, sz, leading=None)
    
    heighty = 520
    widthy = 100
    max_width = 800
    width_dec = 30
    
    
    #header text
    c.drawCentredString(110, 550, course_name + ' Marksheet')
    c.drawCentredString(800, 550, 'H')
    
    #tmp_data = csv.reader(open(report, "rb"))
    tmp_data = csv.reader(report)
    hdngs = next(tmp_data)
    num_cols = len(hdngs)
    
    if num_cols > 35:
        width_dec = 600/num_cols
        sz = 8
        c.setFont(fnt, sz, leading=None)
    elif num_cols > 20:
        width_dec = 600/num_cols
        sz = 10
        c.setFont(fnt, sz, leading=None)
    
    
    #print num_cols
    
    #marks_data = csv.reader(open(report, "rb"))
    marks_data = csv.reader(report)
    for row in marks_data:
        
        heighty -= 20
        
        c.drawCentredString(widthy, heighty, row[0])
        widthy += 70
        
        for k in range(1, num_cols):
            c.drawCentredString(widthy, heighty, row[k])
            widthy += width_dec
            
        widthy = 100
        
        if heighty < 50:
            c.showPage()
            heighty = 550
            c.setFont(fnt, sz, leading=None)
        
    #save pdf page, use for each page
    c.showPage()
    #print 'created'
    c.save()
    return c
    
 
  

