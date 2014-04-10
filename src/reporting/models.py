from django.db import models
    
    
class Module(models.Model):
  module_code = models.CharField(max_length=7)
  module_name = models.CHarField(max_length=255)
  presentation_year = models.IntegerField()
  
  def __unicode__(self):
        return self.module_code

class Assessment(models.Model):
  assessment_id = models.IntegerField()
  module_code = models.ForeignKey(Module)
  assessment_description = models.CHarField(max_length=255)
  is_published = models.IntegerField()
  
  def __unicode__(self):
        return self.assessment_description

class Person(models.Model):
  person_id = models.CharField(max_length=10)
  person_name = models.CharField(max_length=255)
  person_surname = models.CharField(max_length=255)
  
  def __unicode__(self):
        return self.person_name


class MarkAllocation(models.Model):
  assessment_id = models.ForeignKey(Assessment)
  person_id = models.ForeignKey(Person)
  mark = models.DecimalField(max_digits=5, demical_places=5)
  comments = models.CharField(max_length=1024)
  
  def __unicode__(self):
        return self.mark
      
class Audit(models.Models):
  user_id = models.ForeignKey(person)
  assessment_id = models.ForeignKey(Assessment)
  event_action = models.CharField(max_length=50)
  event_date = models.DateTimeField()
  
  def __unicode__(self):
        return self.event_action