from django.shortcuts import render

# Create your views here.
from .models import Property
from django.views.generic import ListView , DetailView

class PropertyList(ListView):
    model = Property