from class_modules.ReportRequest import ReportRequest
from class_modules.ReportGenerator import Report
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


import csv

marks = 'studentMark.csv'

class StudentMarksReport(Report):

 
	def create_report(data_file,course,student):
	    pdf_name = student + ' marks report.pdf'
	    c = canvas.Canvas(pdf_name, pagesize = A4)
	    height = 770
	    width = 30
	    ave_prac = []
	    ave_ct = []
	    count = 0

	    #For PDF
	    c.drawCentredString(110, 800, 'Module: ' + course)
	    c.drawCentredString(120, 780, 'Marks summary for u' + student)
	    
	    #For returning
	    self.doc_heading = 'Module: ' + course
	    self.doc_heading.append('\n' + 'Marks summary for u' + student)
	    #End Returning

	    summary = csv.reader(open(data_file, "rb"))
	    for row in summary:
	        width += 70
	        height -= 20
	        
	        c.drawCentredString(width, height, row[0])
	        width += 70
	        c.drawCentredString(width, height, row[1])
	        width += 70
	        c.drawCentredString(width, height, row[2])
	        width += 40
	        c.drawCentredString(width, height, row[3])
	        width += 40
	        c.drawCentredString(width, height, row[4])
	        width += 40
	        c.drawCentredString(width, height, row[5])

	        count += 1
	        body.append(row)

	        if count == 2:
	        	ave_prac = [int(row[4]),int(row[5])]
	        	ave_ct = [int(row[2]),int(row[3])]

	        width = 30

	    def average(array):
	    	return sum(array) * 1.0 / len(array)

	    avePrac = average(ave_prac)
	    aveCT = average(ave_ct)

	    c.drawCentredString(149, 650, 'Practicals average: ' + str(avePrac))
	    c.drawCentredString(150, 630, 'Class tests average: ' + str(aveCT))

	    #For returning
	    body.append('Practicals average: ' + str(avePrac))
	    body.append('Class tests average: ' + str(aveCT))

	    def returnHeader(self):
			return self.doc_heading

		def returnBody(self):
			return self.body
		#End returning

	    c.showPage()

	    
	    c.save()
	    
	create_report(marks,'COS 332','10125489')
