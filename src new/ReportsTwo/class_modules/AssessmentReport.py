import csv
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report
#from Report import Report

class AssessmentReport(Report):
  def __init__(self,assessment,course):
        self.createReport(assessment,course)
  
  #def average(array):
        #return sum(array) * 1.0 / len(array)
  
  def createReport(self,assessment,course):
	self.doc_heading = "Assessment Report for " + course +" "+assessment
    #self.column_headings = getAssessment(assessment,course) 
	#self.body = getAuditBody(assessment,course)
	#csv in use for now
	total = 0
	#self.count = 0
        assessments = []
        csvreader = csv.reader(open('assessment.csv', "rb"))
	for count, row in enumerate(csvreader):
 		# store the data
 		assessments.append(row)
		#if count > 0 :
                    #total += row[1]
		#count += 1
	#ave = average(total)
	#self.body.append("Average",ave)
	self.body = assessments
  def returnHeader(self):
        return self.doc_heading

  def returnBody(self):
        return self.body

  