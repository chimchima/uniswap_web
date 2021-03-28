from django.shortcuts import render
from django.http import Http404, HttpResponseForbidden, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import subprocess
import sys, os
import time
#from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from . import serializers

def index(request):
    aaa = "aaa"
    return render(request, 'index.html', context={'aaa': aaa})

#@api_view(['GET', 'POST'])

@csrf_exempt
def swap(request):
    token_in = request.POST.get('token_in')
    #print(a)
    #return HttpResponse(a)
    #token_in = int(token_in)
    f = open('myfirst/apps/pinatelonline/in.txt', 'w')
    f.write(token_in)
    f.close
    #token_in = int(token_in)
    #subprocess.run(['cd apps/pinatelonline'])
    subprocess.run(["node", "myfirst/apps/pinatelonline/index.js", token_in])
    #time.sleep(5)
    f1 = open("myfirst/apps/pinatelonline/out.txt", 'r')
    out = f1.read()
    f1.close()
    return HttpResponse(out)


'''
subprocess.run(["node", "index.js"])
file = open("text.txt", 'r')
text = file.read()
file.close()'''