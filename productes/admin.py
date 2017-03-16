from django.contrib import admin

# Register your models here.

from productes.models import *


class DetallInline(admin.StackedInline):
	model = Detall

class CarritoAdmin(admin.ModelAdmin):
	inlines = [ DetallInline, ]


admin.site.register(Producte)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(Detall)

