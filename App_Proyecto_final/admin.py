from django.contrib import admin
from .models import Golosinas,ComboCotillon,Copetin,Disfraz,Avatar
# Register your models here.

admin.site.register(Golosinas)
admin.site.register(Disfraz)
admin.site.register(Copetin)
admin.site.register(ComboCotillon)
admin.site.register(Avatar)