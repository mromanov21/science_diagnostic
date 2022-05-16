python -c "
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'diagnostic.settings'
import django
django.setup()
from django.contrib.auth.management.commands.createsuperuser import get_user_model
User = get_user_model()
user = User.objects.filter(is_superuser=True).first()

if user:
    print('Superuser already in database')
else:
    user = User.objects.create_superuser(
        username='$DJANGO_SUPERUSER_USERNAME',
        email='$DJANGO_SUPERUSER_EMAIL',
        password='$DJANGO_SUPERUSER_PASSWORD',
    )

print('Superuser created')"
