# Generated by Django 4.1.2 on 2022-10-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_banner_background_image_homepage_button_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='button_text',
            field=models.CharField(default='En savoir plus...', help_text='Bouton pour le texte', max_length=50),
        ),
    ]
