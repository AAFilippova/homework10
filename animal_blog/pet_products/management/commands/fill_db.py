from django.core.management.base import BaseCommand

from pet_products.models import ProductCategory
from my_auth.models import BlogUser


class Command(BaseCommand):
    help = "fill db"

    def handle(self, *args, **options):
        try:
            categories = ProductCategory.objects.all()

        # удаление данных
            categories.delete()

        # создание
            nutrition = ProductCategory.objects.create(name='Nutrition')
            accessories = ProductCategory.objects.create(name='Accessories')


            su = BlogUser.objects.filter(username='admin').first()
            if not su:
                BlogUser.objects.create_superuser(
                    username='admin',
                    email='admin@admin.local',
                    password='admin',
                )

            self.stdout.write(
                self.style.SUCCESS('DB is ready')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error filling DB: {e}')
            )