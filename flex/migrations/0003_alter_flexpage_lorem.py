# Generated by Django 4.1.2 on 2022-10-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_lorem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='lorem',
            field=models.TextField(blank=True, default='Aliquam consectetur modi dolorem quiquia dolorem. Sed non adipisci eius. Est eius ipsum aliquam. Non eius neque voluptatem quaerat labore. Ut est porro non.', max_length=500),
        ),
    ]