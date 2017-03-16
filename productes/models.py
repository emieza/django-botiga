from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import date

# Create your models here.

class Producte(models.Model):
	nom = models.CharField(max_length=200)
	preu = models.FloatField(default=0.0)
	def __str__(self):
		return self.nom

class Carrito(models.Model):
	nom = models.CharField(max_length=200,default=str(date.today()))
	obert = models.BooleanField(default=True)
	user = models.ForeignKey(User, blank=True, null=True)
	data = models.DateField(default=date.today())
	def __str__(self):
		return self.nom

class Detall(models.Model):
	producte = models.ForeignKey(Producte)
	carrito = models.ForeignKey(Carrito)
	quantitat = models.FloatField()
	def __str__(self):
		return str(self.carrito.nom)+str(self.producte.nom)
