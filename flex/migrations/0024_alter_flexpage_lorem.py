# Generated by Django 4.1.2 on 2022-10-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0023_alter_flexpage_lorem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='lorem',
            field=models.TextField(blank=True, default='Voluptatem est ut tempora labore. Neque non amet numquam ut. Sed adipisci numquam quisquam labore tempora. Neque labore consectetur non ipsum labore. Ut non non dolore est non voluptatem neque. Dolorem consectetur adipisci non dolore dolor.', max_length=500),
        ),
    ]
