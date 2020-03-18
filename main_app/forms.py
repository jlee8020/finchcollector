# from django.forms import ModelForm
from .models import Finch
from .models import Feeding
from django.forms import ModelForm


class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']