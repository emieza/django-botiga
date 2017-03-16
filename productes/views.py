from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView

from productes.models import Producte, Carrito, Detall

class ProducteListView(ListView):
	model = Producte


def mostra_carrito(request):
	return render(request, "productes/mostra_carrito.html", {} )

def afegeix(request, producte_id):
	carro = Carrito.objects.filter(obert=True).count()
	if( carro ):
		# si hi ha carro obert, l'omplo
		carro = Carrito.objects.filter(obert=True)[0]
	else:
		# si no, el creo
		carro = Carrito()
		carro.nom = "prova"
		carro.save()

	detall = Detall()
	detall.carrito = carro
	detall.producte = Producte.objects.get(pk=producte_id)
	detall.quantitat = 1
	detall.save()

	return render(request, "productes/afegeix.html", {} )
