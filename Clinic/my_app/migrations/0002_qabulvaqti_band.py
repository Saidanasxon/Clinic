# Generated by Django 5.0.2 on 2024-02-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qabulvaqti',
            name='band',
            field=models.BooleanField(default=False),
        ),
    ]