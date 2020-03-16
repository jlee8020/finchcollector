from django.shortcuts import render
from django.http import HttpResponse


class Finch:
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
    return HttpResponse('<h1>This is my finches</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})