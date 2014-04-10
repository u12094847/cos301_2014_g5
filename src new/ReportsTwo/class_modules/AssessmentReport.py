from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report

class AssessmentReport(Report):
  def __init__(self, doc_heading, column_headings, body):
    self.doc_heading = doc_heading
    self.column_headings = column_headings
    self.body = body
  
  def createReport(self):
