# Generated by Django 4.1.2 on 2022-10-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0019_alter_flexpage_lorem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='lorem',
            field=models.TextField(blank=True, default='Dolore aliquam sed ut. Sit eius eius dolor. Quaerat sit est adipisci eius quaerat voluptatem. Consectetur dolore neque modi quiquia eius. Voluptatem dolore velit adipisci quiquia voluptatem sed ut. Tempora velit est dolorem. Dolore dolorem porro quaerat est.', max_length=500),
        ),
    ]
