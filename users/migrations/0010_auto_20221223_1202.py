# Generated by Django 2.2.5 on 2022-12-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20221223_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='Unnamed User', max_length=30, verbose_name='first name'),
        ),
    ]
