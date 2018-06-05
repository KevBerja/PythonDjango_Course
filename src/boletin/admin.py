# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp"]
	#list_display_links = ["nombre"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["email", "nombre"]
	class Meta:
		model = Registrado

admin.site.register(Registrado, AdminRegistrado)