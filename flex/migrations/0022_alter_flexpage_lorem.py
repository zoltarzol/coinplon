# Generated by Django 4.1.2 on 2022-10-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0021_alter_flexpage_lorem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='lorem',
            field=models.TextField(blank=True, default='Sed sed non est. Dolore ipsum modi est. Velit dolore amet modi labore amet magnam. Etincidunt quaerat consectetur quisquam voluptatem quiquia voluptatem. Est porro porro eius amet ipsum quiquia sit. Quiquia adipisci aliquam porro est ut quaerat.', max_length=500),
        ),
    ]
