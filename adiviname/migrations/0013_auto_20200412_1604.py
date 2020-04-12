# Generated by Django 2.1.7 on 2020-04-12 14:04

import adiviname.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adiviname', '0012_game_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameIconBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.ImageField(blank=True, max_length=254, null=True, upload_to=adiviname.models.iconBaseName)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='game',
            name='image_base_updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='icon_base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game', to='adiviname.GameIconBase'),
        ),
    ]