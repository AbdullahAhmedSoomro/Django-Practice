from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SignupMember

# Create your views here.


def getAll(request):
  mymembers = SignupMember.objects.all().values()
#   output = ""
#   for x in mymembers:
#     output += x["firstname"]
#     output += x["lastname"]
#     output += x["email"]
  return HttpResponse(mymembers)

def signupuser(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['email']
  member = SignupMember(firstname=x, lastname=y, email=z)
  member.save()
  return HttpResponse(member)

