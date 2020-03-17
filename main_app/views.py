from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch


class Finches:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
    Finch('Lexie', 'blackrosy', 'Silly little Finch', 2),
    Finch('Marimar', 'Chaffinches', 'Shy Diva', 5),
    Finch('Will', 'House', 'Grumpy Finch', 1),
    Finch('Kirby', 'Java', 'Happy little monster', 1),

]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finches = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch}) 