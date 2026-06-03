from django.contrib import admin
<<<<<<< HEAD
from .models import Pokemon

admin.site.register(Pokemon)
=======
from .models import Pokemon, Trainer

admin.site.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass
>>>>>>> 940edef (Lab 6 completado)
