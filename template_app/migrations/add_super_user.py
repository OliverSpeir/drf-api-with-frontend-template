import os
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('template_app', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = 'dev'
        DJANGO_SU_EMAIL = 'dev@test.com'
        DJANGO_SU_PASSWORD = 'dev'

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]