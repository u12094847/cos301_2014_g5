

class Report:
  __init__(self, doc_heading, column_headings, body):
    self.doc_heading = doc_heading
    self.column_headings = column_headings
    self.body = body
  
  def createReport(self):
    
    
  
    
  def average(array):
    return sum(array) * 1.0 / len(array)
    

  def stdDeviation(array):
    
    
    avg = average(array)
    variance = map(lambda x: (x - avg)**2, s)
    import math
    standard_deviation = math.sqrt(average(variance))
    return standard_deviation
    
    
    
    