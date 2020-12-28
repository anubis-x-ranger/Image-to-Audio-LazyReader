# Generated by Django 3.1.3 on 2020-12-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='language',
            field=models.CharField(choices=[('Hindi', 'hi'), ('Marathi', 'mr'), ('Bengali', 'bn'), ('Tamil', 'ta'), ('Urdu', 'ur'), ('English', 'en')], default=('English', 'en'), max_length=15),
        ),
    ]