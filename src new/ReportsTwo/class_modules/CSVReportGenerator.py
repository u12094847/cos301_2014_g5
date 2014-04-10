import csv
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator

class CSVReportGenerator(ReportGenerator):
  def __init__(self, _request):		#Constructor
    self.reportRequest = _request
  
  #acceptes list of lists in data
  def generateReport(self,course,data):		#This method overrides the one in its superclass
    #implementation goes here

   self.doc_heading = course+".csv"

  fileName = self.doc_heading
  with open(fileName, 'wb') as csvOutPut:
    filewriter = csv.writer(csvOutput, quoting=csv.QUOTE_ALL)

    filewriter.writerow(rowdata)


