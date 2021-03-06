# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo = "WELCOME"
	if request.user.is_authenticated():
		titulo = "Welcome %s " %(request.user)
	form = RegModelForm(request.POST or None)
	context = {
		"titulo": titulo,
		"el_form": form,
		}

	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.nombre:
			instance.nombre = "PERSON"
		instance.save()
		context = {
			"titulo": "Thank you %s!" %(nombre)
		}

		if not nombre:
			context = {
				"titulo": "Thank you %s!" %(email)
			}

		print instance
		print instance.timestamp 

	return render(request, "index.html", context)


def contact(request):
	titulo = "Contact"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key, value in form.cleaned_data.iteritems():
			print key, value
		#for key in form.cleaned_data:
			#print key
			#print form.cleaned_data.get(key)
		form_nombre = form.cleaned_data.get("nombre")
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		asunto = 'Contact form'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
		email_mensaje = "%s: %s Sent by %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto, 
			mensaje_email,
			email_from,
			email_to,
			fail_silently=False
			)
		#print nombre, email, mensaje
	context = {
		"form": form,
		"titulo": titulo,
	}

	return render(request, "forms.html", context)