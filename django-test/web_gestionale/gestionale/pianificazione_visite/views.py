from django.shortcuts import render
from pianificazione_visite.models import Doctor, Visita, societa
from django.views import generic
def index(request):
	num_Doctor = Doctor.objects.all().count()
	num_Visita = Visita.objects.all().count()
	num_societa = societa.objects.all().count()
	num_visita_non_assegnate = Visita.objects.filter(doctor__isnull = True).count()
	context = {
		'num_Doctor' : num_Doctor,
		'num_societa' : num_societa,
		'num_Visita' : num_Visita,
		'num_visita_non_assegnate' : num_visita_non_assegnate,
	}
	
	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)


class DoctorListView(generic.ListView):
    model = Doctor