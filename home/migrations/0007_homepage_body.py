# Generated by Django 4.1.2 on 2022-10-12 14:19

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_homepage_button_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('Title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
