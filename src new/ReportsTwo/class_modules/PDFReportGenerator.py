import pdf
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator
from class_modules.ReportGenerator import Report
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class PDFReportGenerator(ReportGenerator):
  def __init__(self, _request):		#Constructor
    self.reportRequest = _request
  
  def __init__(self,report):		#Constructor
    self.report = report
    create_report(report)
  
  from reportlab.lib.pagesizes import A4

import csv


course_name = 'COS 212'


def create_report(report):
    pdf_name = course_name + ' Marksheet.pdf'
    c = canvas.Canvas(pdf_name, pagesize = A4)
    heighty = 770
    widthy = 30
    #header text
    c.drawCentredString(110, 800, course_name + ' Marksheet')

    marks_data = csv.reader(open(data_file, "rb"))
    for row in marks_data:
        widthy += 70
        heighty -= 20
        
        c.drawCentredString(widthy, heighty, row[0])
        widthy += 70
        c.drawCentredString(widthy, heighty, row[1])
        widthy += 40
        c.drawCentredString(widthy, heighty, row[2])
        widthy += 40
        c.drawCentredString(widthy, heighty, row[3])
        widthy += 40
        c.drawCentredString(widthy, heighty, row[4])
        widthy += 40
        c.drawCentredString(widthy, heighty, row[5])
        widthy += 40
        c.drawCentredString(widthy, heighty, row[6])
        widthy += 40
        c.drawCentredString(widthy, heighty, row[7])
        
        widthy = 30
    #save pdf page, use for each page
    c.showPage()
    #print 'created'
    c.save()
    
 
  

