from itertools import count

from django.shortcuts import render
import json
from . models import Play
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse

def drowchart(request):
    x=['1','2','3','4','5','6','7','8','9']
    y=[12,5,1,16,9,15,8,0,13]
    return render(request,'show_chart.html',{'x': json.dumps(x),'y': json.dumps(y),})


