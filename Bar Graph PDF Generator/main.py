from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors
from reportlab.graphics import renderPDF

import csv

data_file = 'averages.csv'
course_name = 'COS 212'


def create_chart(data_file):
    pdf_name = course_name + ' Bar Chart.pdf'
    drawing = Drawing(400, 200)
    #marks_data = csv.reader(open(data_file, "rb"))
    #for row in marks_data:
    
    data = [
            (89,74,69,63,35,55,48,50),
            (85,73,81,55,60,77,68,61)
            ]

    bc = VerticalBarChart()
    bc.x = 50
    bc.y = 50
    bc.height = 125
    bc.width = 300
    bc.data = data
    bc.strokeColor = colors.black
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 100
    bc.valueAxis.valueStep = 10
    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = 8
    bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.labels.angle = 0
    bc.categoryAxis.categoryNames = ['P1','P2','P3',
    'P4','P5','P6','P7','P8']
    
    drawing.add(bc)
    
    renderPDF.drawToFile(drawing, 'chart.pdf', 'u12747640')
    
create_chart(data_file) 
