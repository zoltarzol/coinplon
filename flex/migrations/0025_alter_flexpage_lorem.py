# Generated by Django 4.1.2 on 2022-10-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0024_alter_flexpage_lorem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='lorem',
            field=models.TextField(blank=True, default='Labore etincidunt ipsum quisquam etincidunt consectetur tempora. Labore consectetur modi dolorem. Magnam dolor consectetur sit consectetur quaerat. Est dolorem non est eius quaerat. Amet dolor voluptatem neque voluptatem.', max_length=500),
        ),
    ]
