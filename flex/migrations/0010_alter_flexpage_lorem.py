# Generated by Django 4.1.2 on 2022-10-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0009_alter_flexpage_lorem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='lorem',
            field=models.TextField(blank=True, default='Dolor dolor labore dolor ipsum labore modi. Modi modi aliquam porro etincidunt sit modi. Etincidunt adipisci quisquam labore est. Neque aliquam porro quisquam est. Numquam sit magnam adipisci ipsum voluptatem. Dolor tempora sed voluptatem. Ut dolorem dolorem etincidunt sit. Voluptatem porro modi neque dolorem adipisci numquam.', max_length=500),
        ),
    ]
