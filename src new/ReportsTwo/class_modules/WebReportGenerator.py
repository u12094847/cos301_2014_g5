from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import ReportGenerator
from class_modules.Report import Report
from class_modules.AuditReport import AuditReport
from class_modules.StudentMarksReport import StudentMarksReport
from class_modules.AssessmentReport import AssessmentReport

class WebReportGenerator(ReportGenerator):
  def __init__(self):		#Constructor
    test = ""
   
  
  def generateReport(self, module, assessment, outputType): #Assessment Report

            if outputType == "object":
                    """
                    BLogicObject = businessLogicAPI()
                    returnedData = BLogicObject.getAllAssessmentsForModule(mod_code)
                    
                    """

  #------------------------After result is returned----------------------------
  
                    reportName = "Assessment Report"
                    headings = ["Student No", "ST1", "ST2", "T1", "T2"]
                    totals = [50, 50, 10, 10]
                    returnedData = [["10122893", 45, 50, 5, 10], ["10392837", 45, 50, 5, 10], ["12748392", 45, 50, 5, 10]]
                    
                    report = AssessmentReport(reportName, headings, totals, returnedData)
                    
                    return report;
            else:
                    return "Error: Incorrect output type"
                  
  #--------------------------------------------------------------------------------------------------
  
  def generateReport(self, module, studentNo, assessments, outputType):  #Student Marks Report
                    """
                    studentNumber = studentNo
                    """
  #------------------------After result is returned----------------------------
                    studentNumber = "10189337"
                    reportName = "Student Marks Report for " + studentNumber 
                    headings = []


  def generateReport(self, module, userID, alteredTable, dateFrom, dateTo, outputType):  #Audit Report
            test = "" #N.B. Remove this line of code when you start
