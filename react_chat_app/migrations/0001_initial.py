# Generated by Django 3.1 on 2021-03-01 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Scream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screams', models.TextField(max_length=1000, null=True)),
                ('date_created', models.DateField(default=django.utils.timezone.now, null=True)),
                ('likes', models.IntegerField(default=0, null=True)),
                ('dislikes', models.IntegerField(default=0, null=True)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('scream_connected', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='react_chat_app.scream')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
