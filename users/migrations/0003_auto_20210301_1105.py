# Generated by Django 3.1 on 2021-03-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210301_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='/default.png', help_text='User Image', null=True, upload_to='chat'),
        ),
    ]
