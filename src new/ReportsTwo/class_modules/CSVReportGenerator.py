import csv
from datetime import datetime
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator
from class_modules.AuditReport import AuditReport
from class_modules.StudentMarksReport import StudentMarksReport
from class_modules.AssessmentReport import AssessmentReport

class CSVReportGenerator(ReportGenerator):
  def __init__(self, _request):		#Constructor
    self.reportRequest = _request

  def generateReport(self, module, assessment, outputType):  #Assessment Report
    if outputType == "csv":
      reportname = "Assessmentcsv_" + module + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
      dataA = getAssessmentMarks(module,assessment)
      dataT = getTotals(module,assessment)
      
      assign = AssessmentReport(reportname,dataA[0],dataT,dataA)
      header = merge(assign.getHeadings,assign.getotals)
      genCSV(assign.getData,header,assign.getReportName)
      return assign.getReportName+".csv"
    
  def generateReport(self, module, studentNo, assessments, outputType):  #Student Marks Report
    if outputType == "csv":
      if assessments != "":
        dataA = getStudentMarks(module,studentNo, assessments)
        dataT = getTotals(module)
      else:
        dataA = getStudentMarks(module,studentNo)
        dataT = getTotals(module)
      
      student = StudentMarksReport(name,headings,totals,data)
      header = merge(student.getHeadings,student.getotals)
      genCSV(student.getData,header,student.getReportName)
      return student.getReportName+".csv"

  def generateReport(self, module, userID, alteredTable, dateFrom, dateTo, outputType):  #Audit Report
    
    if outputType == "csv":
      
      if module != "":
        
        if userID != "":
          
          if alteredTable != "":
            reportname = "Auditcsv_" + module + userID + alteredTable + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
            #date = getUserTableAudit(module,userID,alteredTable,dateFrom,dateTo)
          else:
            reportname = "Auditcsv_" + module + userID + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
            #data = getUserAudit(module,userID,dateFrom,dateTo) 
        else:
          if alteredTable != "":
            reportname = "Auditcsv_" + module + alteredTable + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
            data = getTableAudit(module,alteredTable,dateFrom,dateTo)

      audit = AuditReport(reportName,data[0],data)
      genCSV(audit.getData(),audit.getHeadings(),audit.getReportName())
      
      return audit.getReportName() + ".csv"
    
  def merge(self,header,total):
    count=0
    countb=0
    listH = []
    for i in header:
      if count > 1:
        listH.append(i + "("+total[countb]+")")
      listH.append(i);
    return listH
    
  def genCSV(self,data,headings,name):
    self.doc_heading = name+".csv"
    fileName = self.doc_heading
    
    with open(fileName, 'wb') as csvOutPut:
      filewriter = csv.writer(csvOutput, quoting=csv.QUOTE_ALL)
      filewriter.writerow(headings)
      filewriter.writerow(data)
  
  #return csvOutput

