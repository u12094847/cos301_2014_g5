from django.db import models

class Student(models.Model):
    """List of Enrolled Students"""

    student_nr = models.IntegerField();
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    grades = models.IntegerField();

    def __unicode__(self):
        return self.name
    