import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html", {"year": datetime.datetime.now().year})

def notify(request):
    email = request.POST.get("email")
    # Save email to DB or mailing list here
    return HttpResponse('<div class="text-success fw-semibold">Thanks! We’ll be in touch soon. 🚀</div>')
