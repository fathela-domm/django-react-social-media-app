# Generated by Django 3.1 on 2021-03-12 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('react_chat_app', '0010_auto_20210312_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='scream_connected',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='react_chat_app.scream'),
        ),
    ]
