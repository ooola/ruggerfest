from django.contrib import admin
from models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('teamname', 'division', 'captain', 'email', 'phone_number', 'date', 'paid')

admin.site.register(Team, TeamAdmin)
