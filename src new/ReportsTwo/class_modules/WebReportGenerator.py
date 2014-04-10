from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator
from class_modules.Report import Report
from class_modules.AuditReport import AuditReport
from class_modules.StudentMarksReport import StudentMarksReport
from class_modules.AssessmentReport import AssessmentReport

class WebReportGenerator(ReportGenerator):
  __init__(self, _request):		#Constructor
    self.reportRequest = _request
  
  
  def generateReport(self):		#This method overrides the one in its superclass
    #implementation goes here
