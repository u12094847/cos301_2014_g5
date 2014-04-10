from class_modules.ReportRequest import ReportRequest

class ReportGenerator:
  def __init__(self, _request):		#Constructor
    self.reportRequest = _request
  
  
  def generateReport(self):		#ReportGenerator abstract method. This method will be implemented by respective subclasses
    test = "" #N.B. Remove this line of code when you start coding