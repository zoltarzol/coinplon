# Generated by Django 4.1.2 on 2022-10-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_button_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='button_text',
            field=models.CharField(default='Read more', help_text='Bouton pour le texte', max_length=50),
        ),
    ]