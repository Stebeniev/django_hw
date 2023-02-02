# Generated by Django 4.1.5 on 2023-01-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
