# Generated by Django 4.0.5 on 2022-09-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_missing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
