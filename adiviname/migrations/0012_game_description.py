# Generated by Django 2.1.7 on 2019-11-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adiviname', '0011_auto_20191005_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
