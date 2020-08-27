import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.date.today()
    return render(request, "newyear\index.html", {
        "new_year": now.month == 1 and now.day == 1
    })