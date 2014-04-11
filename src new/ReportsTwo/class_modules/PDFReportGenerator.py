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
  
  def generateReport(self):		#This method overrides the one in its superclass
    #implementation goes here
	
