# Generated by Django 2.2.16 on 2022-06-18 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]