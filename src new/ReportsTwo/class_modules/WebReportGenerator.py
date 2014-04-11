from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator
from class_modules.Report import Report
from class_modules.AuditReport import AuditReport
from class_modules.StudentMarksReport import StudentMarksReport
from class_modules.AssessmentReport import AssessmentReport

class WebReportGenerator(ReportGenerator):
  def __init__(self, _request):		#Constructor
    self.reportRequest = _request
   def __init__(self,report):		#Constructor
    self.report = report
  
  def generateReport(self,report):		#This method overrides the one in its superclass
    #implementation goes here
	return report
