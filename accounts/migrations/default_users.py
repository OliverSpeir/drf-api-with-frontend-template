import environ
from django.db import migrations
from pathlib import Path
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

env = environ.Env(
        ADMIN_USERNAME=(str, "dev1"),
        ADMIN_PASSWORD=(str, "dev1"),
        ADMIN_EMAIL=(str, "admin@test.com"),
        USER_USERNAME=(str, "user1"),
        USER_PASSWORD=(str, "uncommon1"),
        USER_EMAIL=(str, "user@test.com"),
    )
environ.Env.read_env(Path(__file__).resolve().parent.parent.parent / ".env")

def generate_superuser(apps, schema_editor):

    username = env.str("ADMIN_USERNAME")
    password = env.str("ADMIN_PASSWORD")
    email = env.str("ADMIN_EMAIL")

    user = get_user_model()

    admin = user.objects.create_superuser(
       username=username, password=password, email=email
    )
    admin.save()

def generate_user(apps, schema_editor):

    username = env.str("USER_USERNAME")
    password = env.str("USER_PASSWORD")
    email = env.str("USER_EMAIL")

    user = get_user_model()

    new_user = user.objects.create(username=username, password=make_password(password), email=email)
    new_user.save()


class Migration(migrations.Migration):
    dependencies = [("accounts", "0001_initial"),]

    operations = [migrations.RunPython(generate_superuser), migrations.RunPython(generate_user)]
