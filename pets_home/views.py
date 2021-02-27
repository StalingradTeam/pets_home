from django.shortcuts import render, get_object_or_404
from pets_home.models import Pets, TypeOfAnimal
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, DetailView

class HomeView(TemplateView):
	template_name = "home.html"

def index(request):
	template = loader.get_template('index.html')
	pets = Pets.objects.all()
	pets_data = {
		"pets": pets,
	}
	return HttpResponse(template.render(pets_data, request))

def dog_list(request):
	template = loader.get_template('dog_list.html')
	dogs = Pets.objects.filter(type_of_animal__animal_type='Собаки')
	dogs_data = {
		'dogs': dogs,
	}
	return HttpResponse(template.render(dogs_data, request))

def dog(request, pk):
	dogs = get_object_or_404(Pets, pk=pk)
	return render(request, 'dog.html', {'dogs': dogs})

def cat_list(request):
	cats = Pets.objects.filter(type_of_animal__animal_type='Кошки')
	return render(request, 'cat_list.html', {'cats': cats})

def cat(request, pk):
	cats = get_object_or_404(Pets, pk=pk)
	return render(request, 'cat.html', {'cats': cats})

def parrot_list(request):
	parrots = Pets.objects.filter(type_of_animal__animal_type='Птицы')
	return render(request, 'parrot_list.html', {'parrots': parrots})

def parrot(request, pk):
	parrots = get_object_or_404(Pets, pk=pk)
	return render(request, 'parrot.html', {'parrots': parrots})

# Create your views here.
