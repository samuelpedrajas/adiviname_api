# Generated by Django 2.1.7 on 2019-09-27 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adiviname', '0003_gameclick_gametype'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(default='normal', on_delete=django.db.models.deletion.CASCADE, related_name='games', to='adiviname.GameType'),
            preserve_default=False,
        ),
    ]
