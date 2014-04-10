from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report

class StudentMarksReport(Report):
  __init__(self, _request):
    self.request = request
  
  def createReport(self):
