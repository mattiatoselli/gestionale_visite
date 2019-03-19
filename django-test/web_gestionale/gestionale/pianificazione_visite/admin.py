from django.contrib import admin
from pianificazione_visite.models import Doctor
from pianificazione_visite.models import societa
from pianificazione_visite.models import Visita
from pianificazione_visite.models import stazione
from pianificazione_visite.models import contatto
import csv
from django.http import HttpResponse
from django.contrib.auth.models import Group
# Register your models here.
# Define the admin class

class visitaInline(admin.TabularInline):
	model = Visita
	extra = 0
	ordering = ['data']
class contattoInLine(admin.TabularInline):
	model = contatto
	extra = 0

class contattoAdmin(admin.ModelAdmin):
	list_display = ('cognome', 'nome', 'numero_telefonico', 'email', 'societa')
	search_fields = ('cognome', 'nome',)
	class Meta:
		ordering = ['cognome' , 'nome']
		list_per_page = 20
	actions = ["export_as_csv"]

	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])

		return response

	export_as_csv.short_description = "Esporta contatti selezionati"

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('Last_Name', 'Name', 'Email', 'Numero_Telefonico', 'attivo')
	list_filter = ('Sesso',)
	fieldsets =(
		('Informazioni di sistema', {
			'fields': ('attivo',) 
			}),
		('Anagrafica', {
			'fields': ('Name', 'Last_Name', 'Sesso','numero_albo')
			}),
		('Contatti', {
			'fields': (('Email', 'Email_secondaria'), 'Numero_Telefonico', 'Numero_Telefonico_Secondario',)
			}),
		)
	inlines = [visitaInline]
	search_fields = ('Name', 'Last_Name',)
	class Meta:
		ordering = ['Name' , 'Name']
		list_per_page = 20

	actions = ["export_as_csv"]

	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])

		return response

	export_as_csv.short_description = "Esporta l'anagrafica dei dottori selezionati"

class societaAdmin(admin.ModelAdmin):
	list_filter = ('Città',)
	inlines = [contattoInLine]
	fieldsets =(
		('Informazioni e contatti', {
			'fields': (('Name', 'Numero_Telefonico'), ('Email',  'tipologia'),)
			}),
		('Informazioni geografiche', {
			'fields': ('Città', 'Piazza_Via_Corso','indirizzo','Numero_Civico',)
			}),
		)
	search_fields = ('Name',)
	class Meta:
		ordering = ['Name' , 'Città']
		list_per_page = 20
	actions = ["export_as_csv"]

	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])

		return response

	export_as_csv.short_description = "Esporta le società selezionate"

class VisitaAdmin(admin.ModelAdmin):
	list_filter = ('data', 'societa','lavorazione_visita',)
	list_display = ['data', 'societa', 'doctor', 'stazione', 'ora_di_inizio', 'ora_di_fine', 'lavorazione_visita']
	actions = ["export_as_csv"]
	search_fields = ('data',)

	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])

		return response

	export_as_csv.short_description = "Esporta le sessioni di visita selezionate"

	class Meta:
		ordering = ['data', 'ora_di_inizio']
		list_per_page = 20


class stazioneAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	inlines = [visitaInline]
	search_fields = ('Nome',)
	class Meta:
		ordering = ['Nome', 'id']
		list_per_page = 20

	actions = ["export_as_csv"]

	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])

		return response

	export_as_csv.short_description = "Esporta le stazioni selezionate"

# Register the admin class with the associated model
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(societa, societaAdmin)
admin.site.register(Visita, VisitaAdmin)
admin.site.register(stazione, stazioneAdmin)
admin.site.register(contatto, contattoAdmin)