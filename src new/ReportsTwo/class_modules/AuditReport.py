import csv
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report

class AuditReport(Report):
  __init__(self,startDate,endDate,course):
    createReport(startDate,endDate,course)
	
    
  def createReport(self,startDate,endDate,course):
	self.doc_heading = "Audit Report for " + course + "from " + startDate + "to " + endDate
    #self.column_headings = getAuditHeadings(startDate,endDate,course) 
	#self.body = getAuditBody(startDate,endDate,course)
	#csv in use for now
	with open('audit.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	for cnt, row in enumerate(csvreader):
 			# store the data
 			body.append(row)

	def returnHeader(self)
		return self.doc_heading
	
	
	def returnBody(self)
		return self.body
	