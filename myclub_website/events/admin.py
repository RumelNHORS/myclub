from django.contrib import admin
from . models import Venue
from . models import MyClubUser
from . models import Event
from django.contrib.auth.models import Group

#admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)

#Remove Groups
admin.site.unregister(Group)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')
	ordering = ('name',)
	search_fields = ('name', 'address')

