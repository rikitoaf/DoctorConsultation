# Generated by Django 2.2 on 2021-03-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='waiting_status',
            field=models.BooleanField(default=True),
        ),
    ]