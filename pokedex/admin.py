from django.contrib import admin
from .models import Pokemon
from .models import Pokemon, Trainer


class PokemonAdmin(admin.ModelAdmin):
    pass


class TrainerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Trainer, TrainerAdmin)