from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Finch

#CVBs
class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

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
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch}) 