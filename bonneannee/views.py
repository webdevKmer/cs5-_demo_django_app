from django.shortcuts import render
from datetime import datetime
# Create your views here.
now = datetime.now()
day = now.day
month = now.month
year = now.year

def index(request):
    context = {
        "newyear": day==1 and month==1,
        "day": day,
        "month": month,
        "year": year,
    }
    return render(request, 'bonneannee/index.html', context)