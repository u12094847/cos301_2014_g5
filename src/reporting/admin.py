import csv

from django import forms
from django.http import HttpResponse
from django.contrib import admin, messages
from django.conf import settings

from reporting.models import (Student)
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_nr', 'name', 'subject', 'grades',)
    list_filter = ['subject',]
    actions = ('export_selected',)
    
    def export_selected(self, request, queryset):
        """Exports the selected students to a CSV file."""
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Students.csv'
        writer = csv.writer(response)

        headings = ["Student Nr", "Name", "Subject", "Grades",]
        writer.writerow(headings)

        for registrant in queryset:
            row = [registrant.student_nr,
                   registrant.name.encode('utf8'),
                   registrant.subject.encode('utf8'),
                   registrant.grades]
            writer.writerow(row)

        return response
    export_selected.short_description = "Export selected Students"
    
admin.site.register(Student, StudentAdmin)
