from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .constants import MONTHY_CHALLENGES as CHALLENGES

# Create your views here.

def getMonth(request, month):
  return HttpResponse(month)

def getChallenge(request, month):
  response = ""
  if month == "january":
    response = CHALLENGES.JANUARY.value
  elif month == "february":
    response = CHALLENGES.FEBRUARY.value
  elif month == "march":
    response = CHALLENGES.MARCH.value
  elif month == "april":
    response = CHALLENGES.APRIL.value
  elif month == "may":
    response = CHALLENGES.MAY.value
  elif month == "june":
    response = CHALLENGES.JUNE.value
  elif month == "july":
    response = CHALLENGES.JULY.value
  elif month == "august":
    response = CHALLENGES.AUGUST.value
  elif month == "september":
    response = CHALLENGES.SEPTEMBER.value
  elif month == "october":
    response = CHALLENGES.OCTOBER.value
  elif month == "november":
    response = CHALLENGES.NOVEMBER.value
  elif month == "december":
    response = CHALLENGES.DECEMBER.value
  else:
    return HttpResponseNotFound("No such month")

  return HttpResponse(response)
  
