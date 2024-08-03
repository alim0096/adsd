from django.shortcuts import render
from .models import ACCIDENT

# Create your views here.
def web(request):
    context = {}
    return render(request, "web.html", context)

def accident_list(request):
    accidents = ACCIDENT.objects.all()  # Fetching all records from the Accident table
    return render(request, 'web.html', {'accident': accidents})
