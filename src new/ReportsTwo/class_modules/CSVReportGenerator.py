import csv
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator
from class_modules.AuditReport import ReportGenerator
from class_modules.StudentMarksReport import ReportGenerator
from class_modules.AssessmentReport import ReportGenerator

class CSVReportGenerator(ReportGenerator):
  def __init__(self, _request):		#Constructor
    self.reportRequest = _request

  def generateReport(self, module, assessment, outputType):  #Assessment Report
    AuditReport(reportName,headings,data)
    
  def generateReport(self, module, studentNo, assessments, outputType):  #Student Marks Report
    test = "" #N.B. Remove this line of code when you start

  def generateReport(self, module, userID, alteredTable, dateFrom, dateTo, outputType):  #Audit Report
    test = "" #N.B. Remove this line of code when you start
    
  def genCSV(self,data):
    self.doc_heading = course+".csv"
    fileName = self.doc_heading
    
    with open(fileName, 'wb') as csvOutPut:
      filewriter = csv.writer(csvOutput, quoting=csv.QUOTE_ALL)
      filewriter.writerow(rowdata)
  
  #return csvOutput

