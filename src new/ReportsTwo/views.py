import logging

from django.http import Http404, HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
#from reporting import models as m
#from class_modules.AssessmentReport import AssessmentReport

logger = logging.getLogger(__name__)


def home(request, template_name='reporting/home.html',
         current_app=None, extra_context=None):
    """Render the home page."""

    context = {
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

def assessments(request, template_name='reporting/assessments.html',current_app=None, extra_context=None):
    """Render the Assessment page."""
    context = {
        "hello"
    }
    if extra_context is not None:
        context.update(extra_context)
    return HttpResponse("hello there")
    #return TemplateResponse(request, template_name, context,current_app=current_app)