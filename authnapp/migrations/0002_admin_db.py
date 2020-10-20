# Generated by Django 2.2.16 on 2020-10-20 10:53

from django.db import migrations


def forwards_func(apps, schema_editor):
    user = apps.get_model("authnapp", "ShopUser")
    user.objects.create(
        pk=1,
        password="pbkdf2_sha256$150000$Poyfal2RNsKa$AAnI/z9WprCunEwku4YKvIU9lJAVNsQ//rH2K9Qy2YY=",
        is_superuser=True,
        username="admin",
        first_name="Vladimir",
        last_name="Mikulitskii",
        email="mikulex@mail.ru",
        is_staff=True,
        is_active=True,
        date_joined="2020-10-11T10:30:10.234Z",
        avatar="",
        age=35,
        # groups=[],
        # user_permissions=[],
    )


def reverse_func(apps, schema_editor):
    user = apps.get_model("authnapp", "ShopUser")
    # Delete all objects
    user.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [('authnapp', '0001_initial')]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
