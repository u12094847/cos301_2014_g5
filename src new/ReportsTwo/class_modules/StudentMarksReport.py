from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report

class StudentMarksReport(Report):

  doc_heading = "Sudent Marks Report for u"
  column_headings = []
  body = []
  
  def __init__(self, emplID, course):
    self.doc_heading += doc_heading
    self.course = course
  
  def createReport(self, emplID):
    #getPerson("emplID","course")
    colHeadings = []
    colHeadings.append("CT1")
    colHeadings.append("Prac1")
    colHeadings.append("Prac2")
    colHeadings.append("Sem1")
    colHeadings.append("CT2")
    self.column_headings = colHeadings
    
    marks = []
    marks.append(1)
    marks.append(9)
    marks.append(12)
    marks.append(25)
    marks.append(5)
    totals = []
    totals.append(1)
    totals.append(9)
    totals.append(12)
    totals.append(25)
    totals.append(5)