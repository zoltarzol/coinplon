# Generated by Django 4.1.2 on 2022-10-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0008_alter_flexpage_lorem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='lorem',
            field=models.TextField(blank=True, default='Etincidunt dolor quiquia sed modi quiquia magnam. Neque quisquam est magnam aliquam sit. Quisquam numquam magnam magnam sed. Non etincidunt dolor dolorem amet consectetur voluptatem. Sit porro sit non. Labore modi sed ipsum non sit consectetur quisquam.', max_length=500),
        ),
    ]
