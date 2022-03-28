from django import forms
from django.forms import ModelForm
from . models import Venue, Event



#Admin Super User Event Form
class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
		labels = {
		'name': '',
		'event_date': 'DD-MM-YY HO : MN : SC',
		'venue': 'Venue',
		'manager': '',
		'attendees': 'Attendees',
		'description': '',

		}


		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
		'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
		'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
		'manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manager'}),
		'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
		'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
		}
#User Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'attendees', 'description')
		labels = {
		'name': '',
		'event_date': 'DD-MM-YY HO : MN : SC',
		'venue': 'Venue',
		'attendees': 'Attendees',
		'description': '',

		}


		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
		'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
		'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
		'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
		'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
		}



#create a venue form
class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('name', 'address', 'zip_code', 'phone', 'web_site', 'email_address', 'venue_image')
		labels = {
		'name': '',
		'address': '',
		'zip_code': '',
		'phone': '',
		'web_site': '',
		'email_address': '',
		'venue_image': '',


		}


		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
		'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
		'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
		'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
		'web_site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Address'}),
		'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
		}

