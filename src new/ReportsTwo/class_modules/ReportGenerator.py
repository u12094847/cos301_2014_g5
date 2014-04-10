from class_modules.ReportRequest import ReportRequest

class ReportGenerator:
  __init__(self, _request):		#Constructor
    self.reportRequest = _request
  
  
  def generateReport(self):		#ReportGenerator abstract method. This method will be implemented by respective subclasses
    