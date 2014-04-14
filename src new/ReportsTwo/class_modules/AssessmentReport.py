import csv
from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

#from Report import Report

class AssessmentReport(Report):
    reportName = ""
    headings = []
    data = []
    marks = []
    def __init__(self,name,headings,data):
        self.reportName = name
        self.headings = headings
        self.data = data
        marks = []
        for row in data :
            marks.append(row[1])
  
    def getName(self):
        return self.reportName

    def getHeadings(self):
        return self.headings
    def getData(self):
        return self.data
    def getStdDeviation(self):
        return stdDeviation(marks)
    def getAverage(self):
        return average(marks)
    def getChart(self):
        d = Drawing(300, 200)
        chart = VerticalBarChart()
        chart.width = 260
        chart.height = 160
        chart.x = 100
        chart.y = sum(marks)
        chart.data = [[1,2], [3,4]]
        chart.categoryAxis.categoryNames = ['foo', 'bar']
        chart.valueAxis.valueMin = 0

        d.add(chart)
        d.save(fnRoot='test', formats=['png', 'pdf'])
        
        return d

  

  
