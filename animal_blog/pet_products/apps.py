from django.apps import AppConfig


class PetProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pet_products'
    verbose_name = "Pet Products"

    def ready(self):
        from . import signals
        print("Inited signals:", signals, "for", self.name)