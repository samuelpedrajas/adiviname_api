# Generated by Django 2.1.7 on 2020-04-12 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adiviname', '0014_auto_20200412_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='icon_base',
        ),
        migrations.AddField(
            model_name='gameiconbase',
            name='game',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='icon_base', to='adiviname.Game'),
            preserve_default=False,
        ),
    ]
