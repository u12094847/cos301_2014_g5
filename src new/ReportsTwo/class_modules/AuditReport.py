import csv
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report

class AuditReport(Report):
  reportName=""
  headings=""
  data=""
  
  def __init__(self,reportName,headings,data):
    self.reportName = reportName
    self.headings = headings
    self.data = data
  
  def getReportName(self):
    return self.reportName

  def getData(self):
    return self.data

  def getHeadings(self):
    return self.headings
