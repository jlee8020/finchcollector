from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Finch, Toy
from .forms import FeedingForm


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
    

# finches = [
#     Finch('Lexie', 'blackrosy', 'Silly little Finch', 2),
#     Finch('Marimar', 'Chaffinches', 'Shy Diva', 5),
#     Finch('Will', 'House', 'Grumpy Finch', 1),
#     Finch('Kirby', 'Java', 'Happy little monster', 1),

# ]
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
    feeding_form = FeedingForm()
    toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
    return render(request, 'finches/detail.html', {
      'finch': finch, 
      'feeding_form': feeding_form,
      'toys': toys_finch_doesnt_have
    
    }) 
def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)


def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'