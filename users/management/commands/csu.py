from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='sjwjnsjknkc',
            email='admin22@sky1.pro',
            avatar='main_app/products/2023-12-27_14.00.53.jpg',
            phone='1234567890',
            city='City Name',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123qwe456rty')
        user.save()