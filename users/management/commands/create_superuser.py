from django.core.management import BaseCommand

from users.models import User


#кастомная команда для создания суперUser
class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email = '2@admin.ru',
            first_name = 'Admin',
            last_name = 'Admin',
            is_staff = True,
            is_superuser = True,
            is_active = True
        )
        user.set_password('spartak67')  #установка пароля
        user.save()  # сохраниние в БД


