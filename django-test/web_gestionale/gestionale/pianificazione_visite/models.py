from django.db import models
import uuid # Required for unique id in doctors and societa
from django.urls import reverse
from django.core.exceptions import ValidationError
import re
# Create your models here.
# define data structure of pianificazione_visite app
class Doctor(models.Model):
	"""Model representing a Doctor."""
	Name = models.CharField(max_length=50, verbose_name='Nome', null=True, blank=False)
	Last_Name = models.CharField(max_length=50, verbose_name='Cognome', null=True, blank=False)
	Email = models.EmailField(max_length=90, null=True, blank=False)
	attivo=models.BooleanField(default=True, help_text='Il medico lavora attualmente per noi?')
	Email_secondaria = models.EmailField(max_length=90, null=True, blank=True, verbose_name='Email Secondaria')
	Numero_Telefonico = models.CharField(max_length=11, null=True, blank=False)
	Numero_Telefonico_Secondario = models.CharField(max_length=11, null=True, blank=True, verbose_name='Numero telefonico secondario')
	numero_albo = models.CharField(max_length = 12, verbose_name='Numero di Iscrizione all\'albo', null=True, blank=False)
	Sesso = models.CharField(
		max_length=1,
		choices=(('m','Maschio'), ('f', 'Femmina')),
		blank=True,
		default='m',
		help_text='Sesso del medico',
		)
	Set_provinces= (
		('AG', 'AGRIGENTO'),
		('AN', 'ANCONA'),
		('AO', 'AOSTA'),
		('AQ', 'L\'AQUILA'),
		('AG', 'AGRIGENTO'),
		('AR','AREZZO'),
		('AP', 'ASCOLI-PICENO'),
		('AT', 'ASTI'),
		('AV', 'AVELLINO'),
		('BA', 'BARI'),
		('BT', 'BARLETTA'),
		('BL', 'BELLUNO'),
		('BN','BENEVENTO'),
		('BG', 'BERGAMO'),
		('BI', 'BIELLA'),
		('BO', 'BOLOGNA'),
		('BZ', 'BOLZANO'),
		('BS', 'BRESCIA'),
		('BR', 'BRINDISI'),
		('CA','CAGLIARI'),
		('CL', 'CALTANISETTA'),
		('CB', 'CAMPOBASSO'),
		('CI', 'CARBONIA IGLESIAS'),
		('CE', 'CASERTA'),
		('CT', 'CATANIA'),
		('CZ', 'CATANZARO'),
		('CH', 'CHIETI'),
		('CO', 'COMO'),
		('CS', 'COSENZA'),
		('CR', 'CREMONA'),
		('KR','CROTONE'),
		('CN', 'CUNEO'),
		('EN', 'ENNA'),
		('FM', 'FERMO'),
		('FE', 'FERRARA'),
		('FI', 'FIRENZE'),
		('FG', 'FOGGIA'),
		('FC', 'FORLI-CESENA'),
		('FR', 'FROSINONE'),
		('GE', 'GENOVA'),
		('GO', 'GORIZIA'),
		('GR','GROSSETO'),
		('IM', 'IMPERIA'),
		('IS', 'ISERNIA'),
		('SP', 'LA SPEZIA'),
		('LT', 'LATINA'),
		('LE', 'LECCE'),
		('LC', 'LECCO'),
		('LI', 'LIVORNO'),
		('LO', 'LODI'),
		('LU', 'LUCCA'),
		('MC', 'MACERATA'),
		('MN', 'MANTOVA'),
		('MS','MASSA CARRARA'),
		('MT', 'MATERA'),
		('MI', 'MILANO'),
		('MO', 'MODENA'),
		('MB', 'MONZA BRIANZA'),
		('NA', 'NAPOLI'),
		('NO', 'NOVARA'),
		('NU', 'NUORO'),
		('OG', 'OGLIASTRA'),
		('OT', 'OLBIA TEMPIO'),
		('OR', 'ORISTANO'),
		('PD','PADOVA'),
		('PA', 'PALERMO'),
		('PR', 'PARMA'),
		('PV', 'PAVIA'),
		('PG', 'PERUGIA'),
		('PU', 'PESARO URBINO'),
		('PE', 'PESCARA'),
		('PC', 'PIACENZA'),
		('PI', 'PISA'),
		('PT', 'PISTOIA'),
		('PN', 'PORDENONE'),
		('PZ', 'POTENZA'),
		('PO', 'PRATO'),
		('RG','RAGUSA'),
		('RA', 'RAVENNA'),
		('RC', 'REGGIO CALABRIA'),
		('RE', 'REGGIO EMILIA'),
		('RI', 'RIETI'),
		('RN', 'RIMINI'),
		('ROMA', 'ROMA'),
		('RO', 'ROVIGO'),
		('SA', 'SALERNO'),
		('SS', 'SASSARI'),
		('SV', 'SAVONA'),
		('SI', 'SIENA'),
		('SR', 'SIRACUSA'),
		('SO', 'SONDRIO'),
		('TA', 'TARANTO'),
		('TE', 'TERAMO'),
		('TR', 'TERNI'),
		('TO', 'TORINO'),
		('TP', 'TRAPANI'),
		('TN', 'TRENTO'),
		('TV', 'TREVISO'),
		('TS', 'TRIESTE'),
		('UD', 'UDINE'),
		('VA', 'VARESE'),
		('VE', 'VENEZIA'),
		('VB', 'VERBANIA'),
		('VC', 'VERCELLI'),
		('VR', 'VERONA'),
		('VV', 'VIBO VALENTIA'),
		('VI', 'VICENZA'),
		('VT', 'VITERBO'),
		)
	class Meta:
		ordering = ['Last_Name' , 'Name']
		verbose_name = "Dottore"
		verbose_name_plural = "Dottori"
	#def __str__(self):
	#		return f'{self.Last_Name} {self.Name}'
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of the model."""
		return reverse('model-detail-view', args=[str(self.id)])
	def clean(self):
		#check for non void string in phonenumber, or a valid number
		if not self.Numero_Telefonico:
			raise ValidationError('Inserire un numero di telefono! I campi in grassetto sono obbligatori.')
		for number in self.Numero_Telefonico:
			if number.isdigit() is False:
				raise ValidationError('Inserire solamente numeri nel campo dei contatti telefonici')
		if len(self.Numero_Telefonico) != 9 and len(self.Numero_Telefonico) != 10:
			raise ValidationError('inserire un numero a 9 o 10 cifre nei campi telefonici')
		if self.Numero_Telefonico_Secondario:
			for number in self.Numero_Telefonico_Secondario:
				if number.isdigit() is False:
					raise ValidationError('Inserire solamente numeri nel campo dei contatti telefonici')
			if len(self.Numero_Telefonico_Secondario) != 9 and len(self.Numero_Telefonico_Secondario) != 10:
				raise ValidationError('inserire un numero a 9 o 10 cifre nei campi telefonici')
		if not self.numero_albo:
			raise ValidationError('Il numero di iscrizione albo è obbligatorio!')
		for number in self.numero_albo:
			if number.isdigit() is False:
				raise ValidationError('Il numero di iscrizione all\'albo deve essere composto solo da cifre!')
		query_avoid_duplicates = Doctor.objects.filter(Name = self.Name.capitalize(), Last_Name=self.Last_Name.capitalize(), numero_albo=self.numero_albo).exclude(id=self.id)
		if query_avoid_duplicates.exists():
			raise ValidationError('Il medico esiste già nel database!')
		query_avoid_duplicates = Doctor.objects.filter(numero_albo=self.numero_albo).exclude(id=self.id)
		if query_avoid_duplicates.exists():
			raise ValidationError('Esiste già un medico con questo numero di iscrizione all\'albo, tale valore deve essere univoco!')

	def save(self, force_insert=False, force_update=False):
		newName=self.Name.capitalize()
		newLastName=self.Last_Name.capitalize()
		self.Name = newName
		self.Last_Name = newLastName
		super(Doctor, self).save()



#modello per le società sportive
class societa(models.Model):
	"""Model representing a customer."""
	Name = models.CharField(max_length=100, verbose_name='Nome Società', null=True, blank=False, help_text='Nome Società.' )
	Piazza_Via_Corso = models.CharField(
		max_length=10,
		choices=(('Via','Via'), ('Viale', 'Viale'),('Corso', 'Corso'), ('Piazza', 'Piazza'), ('Largo','Largo'), ('Strada', 'Strada'), ('Altro','Altro (specificare sotto)')),
		blank=True,
		default='vi',
		)
	indirizzo= models.CharField(max_length=100, verbose_name='Nome strada o via/corso', null=True, blank=False)
	Città= models.CharField(max_length=50, verbose_name='Città', null=True, blank=False)
	Numero_Civico = models.CharField(max_length=10, verbose_name='N° Civico', null=True, blank=False)
	attiva = models.BooleanField(default=True, help_text='La società è nostra cliente attualmente?')
	Set_provinces= (
		('AG', 'AGRIGENTO'),
		('AN', 'ANCONA'),
		('AO', 'AOSTA'),
		('AQ', 'L\'AQUILA'),
		('AR','AREZZO'),
		('AP', 'ASCOLI-PICENO'),
		('AT', 'ASTI'),
		('AV', 'AVELLINO'),
		('BA', 'BARI'),
		('BT', 'BARLETTA'),
		('BL', 'BELLUNO'),
		('BN','BENEVENTO'),
		('BG', 'BERGAMO'),
		('BI', 'BIELLA'),
		('BO', 'BOLOGNA'),
		('BZ', 'BOLZANO'),
		('BS', 'BRESCIA'),
		('BR', 'BRINDISI'),
		('CA','CAGLIARI'),
		('CL', 'CALTANISETTA'),
		('CB', 'CAMPOBASSO'),
		('CI', 'CARBONIA IGLESIAS'),
		('CE', 'CASERTA'),
		('CT', 'CATANIA'),
		('CZ', 'CATANZARO'),
		('CH', 'CHIETI'),
		('CO', 'COMO'),
		('CS', 'COSENZA'),
		('CR', 'CREMONA'),
		('KR','CROTONE'),
		('CN', 'CUNEO'),
		('EN', 'ENNA'),
		('FM', 'FERMO'),
		('FE', 'FERRARA'),
		('FI', 'FIRENZE'),
		('FG', 'FOGGIA'),
		('FC', 'FORLI-CESENA'),
		('FR', 'FROSINONE'),
		('GE', 'GENOVA'),
		('GO', 'GORIZIA'),
		('GR','GROSSETO'),
		('IM', 'IMPERIA'),
		('IS', 'ISERNIA'),
		('SP', 'LA SPEZIA'),
		('LT', 'LATINA'),
		('LE', 'LECCE'),
		('LC', 'LECCO'),
		('LI', 'LIVORNO'),
		('LO', 'LODI'),
		('LU', 'LUCCA'),
		('MC', 'MACERATA'),
		('MN', 'MANTOVA'),
		('MS','MASSA CARRARA'),
		('MT', 'MATERA'),
		('MI', 'MILANO'),
		('MO', 'MODENA'),
		('MB', 'MONZA BRIANZA'),
		('NA', 'NAPOLI'),
		('NO', 'NOVARA'),
		('NU', 'NUORO'),
		('OG', 'OGLIASTRA'),
		('OT', 'OLBIA TEMPIO'),
		('OR', 'ORISTANO'),
		('PD','PADOVA'),
		('PA', 'PALERMO'),
		('PR', 'PARMA'),
		('PV', 'PAVIA'),
		('PG', 'PERUGIA'),
		('PU', 'PESARO URBINO'),
		('PE', 'PESCARA'),
		('PC', 'PIACENZA'),
		('PI', 'PISA'),
		('PT', 'PISTOIA'),
		('PN', 'PORDENONE'),
		('PZ', 'POTENZA'),
		('PO', 'PRATO'),
		('RG','RAGUSA'),
		('RA', 'RAVENNA'),
		('RC', 'REGGIO CALABRIA'),
		('RE', 'REGGIO EMILIA'),
		('RI', 'RIETI'),
		('RN', 'RIMINI'),
		('ROMA', 'ROMA'),
		('RO', 'ROVIGO'),
		('SA', 'SALERNO'),
		('SS', 'SASSARI'),
		('SV', 'SAVONA'),
		('SI', 'SIENA'),
		('SR', 'SIRACUSA'),
		('SO', 'SONDRIO'),
		('TA', 'TARANTO'),
		('TE', 'TERAMO'),
		('TR', 'TERNI'),
		('TO', 'TORINO'),
		('TP', 'TRAPANI'),
		('TN', 'TRENTO'),
		('TV', 'TREVISO'),
		('TS', 'TRIESTE'),
		('UD', 'UDINE'),
		('VA', 'VARESE'),
		('VE', 'VENEZIA'),
		('VB', 'VERBANIA'),
		('VC', 'VERCELLI'),
		('VR', 'VERONA'),
		('VV', 'VIBO VALENTIA'),
		('VI', 'VICENZA'),
		('VT', 'VITERBO'),
		)
	tipologia = models.CharField(
		max_length=11,
		choices=(('pa','Palestra'), ('ss', 'Società Sportiva'), ('pi', 'Piscina'), ('al', 'altro')),
		blank=True,
		default='pa',
		)
	Email = models.EmailField(max_length=90, null=True, blank=False, help_text='inserire un indirizzo mail valido.')
	Email_secondaria = models.EmailField(max_length=90, null=True, blank=True, verbose_name='Email Secondaria', help_text='inserire un eventuale seconda Email.')
	Numero_Telefonico = models.CharField(max_length=11, null=True, blank=False)
	Numero_Telefonico_Secondario = models.CharField(max_length=11, null=True, blank=True, verbose_name='Numero telefonico secondario', help_text='Eventuale numero telefonico secondario')
	class Meta:
		ordering = ['Name']
		verbose_name = "Società"
		verbose_name_plural = "Società"
	def clean(self):
		if not self.Numero_Telefonico:
			raise ValidationError('Inserire un numero di telefono! I campi in grassetto sono obbligatori.')
		for number in self.Numero_Telefonico:
			if number.isdigit() is False:
				raise ValidationError('Inserire solamente numeri nel campo dei contatti telefonici')
		if len(self.Numero_Telefonico) != 9 and len(self.Numero_Telefonico) != 10:
			raise ValidationError('inserire un numero a 9 o 10 cifre nei campi telefonici')
		if self.Numero_Telefonico_Secondario:
			for number in self.Numero_Telefonico_Secondario:
				if number.isdigit() is False:
					raise ValidationError('Inserire solamente numeri nel campo dei contatti telefonici')
			if len(self.Numero_Telefonico_Secondario) != 9 and len(self.Numero_Telefonico_Secondario) != 10:
				raise ValidationError('inserire un numero a 9 o 10 cifre nei campi telefonici')
		if not self.indirizzo:
			raise ValidationError('Il campo indirizzo è obbligatorio!')
		indirizzo_capitalized=''

	def __str__(self):
		return f'{self.Name}'
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of the model."""
		return reverse('model-detail-view', args=[str(self.id)])


class contatto(models.Model):
	nome = models.CharField(max_length=50, null=True,blank=False)
	cognome = models.CharField(max_length=50,null=True,blank=False)
	email = models.EmailField(max_length=90, null=True, blank=True)
	numero_telefonico = models.CharField(max_length=11, null=True, blank=False)
	societa = models.ForeignKey(societa, on_delete=models.CASCADE, null=True, blank=False, limit_choices_to={'attiva' : True},)
	class Meta:
		ordering = ['cognome' , 'nome']
		verbose_name = "Contatto"
		verbose_name_plural = "Contatti"
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of the model."""
		return reverse('model-detail-view', args=[str(self.id)])
	def clean(self):
		#check for non void string in phonenumber, or a valid number
		if not self.numero_telefonico:
			raise ValidationError('Inserire un numero di telefono! I campi in grassetto sono obbligatori.')
		for number in self.numero_telefonico:
			if number.isdigit() is False:
				raise ValidationError('Inserire solamente numeri nel campo dei contatti telefonici')
		if len(self.numero_telefonico) != 9 and len(self.numero_telefonico) != 10:
			raise ValidationError('inserire un numero a 9 o 10 cifre nei campi telefonici')
	def save(self, force_insert=False, force_update=False):
		newName=self.nome.capitalize()
		newLastName=self.cognome.capitalize()
		self.nome = newName
		self.cognome = newLastName
		super(contatto, self).save()
	def __str__(self):
			return f'{self.nome} {self.cognome}'



class stazione(models.Model):
	Nome = models.CharField(max_length=15, null=True, blank=False)
	SET_STATUS = (
		('Disponibile', 'Disponibile'),
		('Manutenzione', 'Manutenzione'),
		('Disattivata', 'Disattivata'),
		)


	status = models.CharField(
		max_length=15,
		choices=SET_STATUS,
		blank=False,
		default='Disponibile',)
	class Meta:
		ordering = ['Nome']
		verbose_name='Stazione'
		verbose_name_plural = 'Stazioni'
	def __str__(self):
		return f'{self.Nome}'
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of the model."""
		return reverse('model-detail-view', args=[str(self.id)])

class Visita(models.Model):
	data = models.DateField()
	ora_di_inizio = models.TimeField(null=True, blank=False, verbose_name='Orario di inizio', help_text='inserire in formato hh:mm:ss')
	ora_di_fine = models.TimeField(null=True, blank=False, verbose_name='Orario di fine', help_text='inserire il dato in formato hh:mm:ss')
	# Foreign Key used because visita can only have one medico, but medici can have multiple visita
	doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'attivo': True}, verbose_name='Medico assegnato')
	societa = models.ForeignKey(societa, on_delete=models.SET_NULL, null=True, limit_choices_to={'attiva' : True},)
	stazione = models.ForeignKey(stazione, on_delete=models.SET_NULL, null=True, limit_choices_to={'status': 'Disponibile'},)
	STATUS_FASE =( 
		('Da_iniziare', 'Da Iniziare'),
		('ECG_parziali','ECG Parzialmente inviati'),
		('ECG_ricevuti','ECG ricevuti'),
		('ECG_da_assegnare', 'ECG da assegnare'),
		('ECG_assegnati', 'ECG assegnati'),
		('ECG_parzialmente', 'ECG parzialmente refertati'),
		('ECG_refertati', 'ECG refertati'),
		('Visite_stampate', 'Visite stampate'),
		('Visite_inviate', 'Visite Inviate'),
		('Chiusa', 'Chiusa'),
		)
	lavorazione_visita=models.CharField(
		max_length=25,
		choices=STATUS_FASE,
		blank=False,
		default='Da_iniziare',
		help_text='inserire la fase di lavorazione della sessione di visita',
		)
	note = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		ordering = ['data', 'ora_di_inizio', 'id']
		verbose_name = "Visita"
		verbose_name_plural = "Visite"
	def clean(self):
		if self.doctor:
			query_avoid_duplicates = Visita.objects.filter(doctor=self.doctor, data=self.data).exclude(id=self.id)
			if query_avoid_duplicates.exists():
				for visita in query_avoid_duplicates:
					if self.ora_di_inizio>=visita.ora_di_inizio and self.ora_di_inizio<=visita.ora_di_fine or self.ora_di_fine<=visita.ora_di_fine and self.ora_di_inizio<=visita.ora_di_inizio or self.ora_di_inizio<=visita.ora_di_inizio and self.ora_di_fine>=visita.ora_di_fine:
						if self.id != visita.id:
							raise ValidationError('il medico in questi orari è già impegnato altrove!')
		if self.stazione:
			query_avoid_duplicates = Visita.objects.filter(stazione=self.stazione, data=self.data).exclude(id=self.id)
			for visita in query_avoid_duplicates:
				if self.ora_di_inizio>=visita.ora_di_inizio and self.ora_di_inizio<=visita.ora_di_fine or self.ora_di_fine<=visita.ora_di_fine and self.ora_di_inizio<=visita.ora_di_inizio or self.ora_di_inizio<=visita.ora_di_inizio and self.ora_di_fine>=visita.ora_di_fine:
						if self.id != visita.id:
							raise ValidationError('Questa stazione è già in uso in questi orari!')
	def __str__(self):
		return f'({self.data}) ({self.ora_di_inizio}) ({self.doctor})'
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of the model."""
		return reverse('model-detail-view', args=[str(self.id)])
